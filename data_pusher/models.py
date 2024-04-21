from sqlalchemy import Column, ForeignKey, Integer, String, UUID, JSON
from sqlalchemy.orm import relationship
from data_pusher.database import Base
import uuid


class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    app_secret_token = Column(UUID, unique=True, nullable=False, default=uuid.uuid4)

    destinations = relationship("Destinations", back_populates="account", cascade="all, delete-orphan")


class Destinations(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"))
    url = Column(String, nullable=False)
    http_method = Column(String, nullable=False)
    headers = Column(JSON, nullable=False)

    account = relationship("Accounts", back_populates="destinations")
