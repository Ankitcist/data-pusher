from pydantic import BaseModel
from uuid import UUID


class Account(BaseModel):
    email: str
    name: str


class AccountResponse(Account):
    id: int
    app_secret_token: UUID

    class Config:
        from_attributes = True


class Destination(BaseModel):
    account_id: int
    url: str
    http_method: str
    headers: dict

    class Config:
        from_attributes = True


class ServerIncomingData(BaseModel):
    data: dict






