import json
import requests
from typing import Union
from sqlalchemy.sql import select
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from sql_app.models import *
from sql_app.database import *
from users import *
from sqlalchemy.orm import Session


async def create_user(request: Request):
    data = await request.json()
    session = Session(bind=engine)
    notes = Notes(**data)
    session.add(notes)
    session.commit()
    session.close()
    return {"message": "Notes ajouté à la base de données"}