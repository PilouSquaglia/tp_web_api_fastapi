import json
import requests
from typing import Union
from sqlalchemy.sql import select
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from sql_app.models import *
from sql_app.database import *
from sqlalchemy.orm import Session


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/")
def returnUsers(db: Session = Depends(get_db)):
    res = db.query(User).all()
    return [dict(row) for row in res]

@app.post("/users/")
async def create_user(request: Request):
    data = await request.json()
    session = Session(bind=engine)
    user = User(**data)
    session.add(user)
    session.commit()
    session.close()
    return {"message": "User added to the database"}
