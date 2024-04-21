from fastapi import APIRouter
from typing import List, Optional
from fastapi import Depends, HTTPException, Response
from sqlalchemy.orm import Session
from data_pusher import models, schemas
from data_pusher.database import SessionLocal
from data_pusher.services import AccountsService, DestinationsService


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

""" APIs """
# Accounts
@router.post("/accounts/", response_model=schemas.Account)
async def create_account(account: schemas.Account, db: Session = Depends(get_db)):
    try:
        return AccountsService().create_account(account, db)
    except:
        raise HTTPException(status_code=500, detail="something went wrong")

@router.get('/accounts/', response_model=List[schemas.AccountResponse])
async def get_all_accounts(db: Session = Depends(get_db)):
    try:
        return AccountsService().get_all_accounts(db)
    except:
        raise HTTPException(status_code=500, detail="something went wrong")


@router.put('/accounts/{account_id}', response_model=schemas.Account)
async def update_account(account_id: int, account: schemas.Account, db: Session = Depends(get_db)):
    try:
        account = AccountsService().update_account(account_id, account, db)
        return account
    except:
        raise HTTPException(status_code=404, detail="Account not found")

@router.delete('/accounts/{account_id}', response_model=schemas.Account)
async def delete_account(account_id: int, account: schemas.Account, db: Session = Depends(get_db)):
    try:
        account = AccountsService().delete_account(account_id, account, db)
        return account
    except:
        raise HTTPException(status_code=404, detail="Account not found")


# Destinastions
@router.post("/destinations/", response_model=schemas.Destination)
async def create_destination(destination: schemas.Destination, db: Session = Depends(get_db)):
    try:
        account = AccountsService().get_account_by_id(destination.account_id, db)
        if account == None:
            raise HTTPException(status_code=404, detail="Account not found")
        
        return DestinationsService().create_destination(destination, db)
    except HTTPException as http_exc:
        raise http_exc
    except:
        raise HTTPException(status_code=500, detail="something went wrong or given account_id not exist")

@router.get('/destinations/', response_model=List[schemas.Destination])
async def get_all_destinations(db: Session = Depends(get_db)):
    try:
        return DestinationsService().get_all_destinations(db)
    except:
        raise HTTPException(status_code=500, detail="something went wrong")

@router.put('/destinations/{destination_id}', response_model=schemas.Destination)
async def update_destinations(destination_id: int, destination: schemas.Destination, db: Session = Depends(get_db)):
    try:
        account = AccountsService().get_account_by_id(destination.account_id, db)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        destination = DestinationsService().update_destinations(destination_id, destination, db)
        return destination
    except HTTPException as http_exc:
        raise http_exc
    except:
        raise HTTPException(status_code=500, detail="something went wrong or given account_id or destination_id are not exist")

@router.delete('/destinations/{destination_id}', response_model=schemas.Destination)
async def delete_destination(destination_id: int, destination: schemas.Destination, db: Session = Depends(get_db)):
    try:
        destination = DestinationsService().delete_destination(destination_id, destination, db)
        return destination
    except:
        raise HTTPException(status_code=404, detail="Destination not found")


@router.get('/destinations/accounts/{account_id}', response_model=List[schemas.Destination])
async def get_destinations_by_account_id(account_id : int, db: Session = Depends(get_db)):
    try:
        destinations = DestinationsService().get_destinations_by_account_id(account_id, db)
        
        if not destinations:
            raise HTTPException(status_code=404, detail="Destination not found")
        return destinations
    except HTTPException as http_exc:
        raise http_exc
    except:
        raise HTTPException(status_code=500, detail="Something went wrong")
    

# Data pusher
@router.post('/server/incoming_data/')
async def receive_data(incoming_data: schemas.ServerIncomingData, app_secret_token: str = None, db: Session = Depends(get_db)):
    try:
        if not app_secret_token:
            raise HTTPException(status_code=401, detail="Unauthenticated")
        
        account = AccountsService().get_account_by_app_secret_token(app_secret_token, db)
        if not account:
            raise HTTPException(status_code=404, detail="app_secret_token not found")
        
        destinations = DestinationsService().get_destinations_by_account_id(account.id, db)
        if not destinations:
            raise HTTPException(status_code=404, detail="No destinations found for the given app_secret_token")
        
        DestinationsService().send_data_to_destinations(incoming_data, destinations, db)
        return Response(status_code=200, content="success")
    except HTTPException as http_exc:
        raise http_exc
    except Exception as ex:
        raise HTTPException(status_code=500, detail="something went wrong")


@router.get('/server/incoming_data/')
async def receive_data():
    raise HTTPException(status_code=400, detail="Invalid request method. Use POST method to send data.")

