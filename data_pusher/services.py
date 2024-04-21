import requests
from fastapi import Depends
# from sqlalchemy import UUID
from sqlalchemy.orm import Session
from data_pusher import models


class AccountsService:
    def create_account(self, account, db):
        new_account = models.Accounts(email=account.email, name=account.name)
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return new_account
    
    def get_all_accounts(self, db):
        return db.query(models.Accounts).all()
    
    def update_account(self, account_id, account, db):
        db_account = db.query(models.Accounts).filter(models.Accounts.id == account_id).first()
        db_account.email = account.email
        db_account.name = account.name
        db.commit()
        db.refresh(db_account)
        return db_account
    
    def delete_account(self, account_id, account, db):
        db_account = db.query(models.Accounts).filter(models.Accounts.id == account_id).first()
        db.delete(db_account)
        db.commit()
        return db_account
    
    def get_account_by_app_secret_token(self, app_secret_token, db):
        import uuid
        app_secret_token = uuid.UUID(app_secret_token)
        account = db.query(models.Accounts).filter(models.Accounts.app_secret_token == app_secret_token).first()
        return account
    
    def get_account_by_id(self, id, db):
        account_id = db.query(models.Accounts).filter(models.Accounts.id == id).first()
        return account_id


class DestinationsService:
    def create_destination(self, destination, db):
        new_destination = models.Destinations(account_id=destination.account_id, url=destination.url, http_method=destination.http_method, headers=destination.headers)
        db.add(new_destination)
        db.commit()
        db.refresh(new_destination)
        return new_destination
    
    def get_all_destinations(self, db):
        return db.query(models.Destinations).all()

    def update_destinations(self, destination_id, destination, db):
        db_destination = db.query(models.Destinations).filter(models.Destinations.id == destination_id).first()
        db_destination.account_id = destination.account_id
        db_destination.url = destination.url
        db_destination.http_method = destination.http_method
        db_destination.headers = destination.headers
        db.commit()
        db.refresh(db_destination)
        return db_destination

    def delete_destination(self, destination_id, destination, db):
        db_destination = db.query(models.Destinations).filter(models.Destinations.id == destination_id).first()
        db.delete(db_destination)
        db.commit()
        return db_destination
    
    def get_destinations_by_account_id(self, account, db):
        return db.query(models.Destinations).filter(models.Destinations.account_id == account.id).all()
    
    def send_data_to_destinations(self, data, destinations, db):
        for dest in destinations:
            print(dest.http_method, dest.url, data.data)
            try:
                requests.request(method=dest.http_method, url=dest.url, data=data.data)
            except:
                continue
        
