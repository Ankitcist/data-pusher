from data_pusher import models
from fastapi import FastAPI
from data_pusher.database import engine
from data_pusher.urls import router


# Bind daatbase to models
models.Base.metadata.create_all(bind=engine)

# Create fastapi app and bind api endpoint to the app
app = FastAPI()
app.include_router(router)
