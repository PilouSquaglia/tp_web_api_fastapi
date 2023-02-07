import json
import requests
from typing import Union
from sqlalchemy.sql import select
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from sql_app.models import *
from sql_app.database import *
from sqlalchemy.orm import Session
from faker import Faker

# fake = Faker(['fr_FR'])
# for i in range(10):
#     print(fake.name())

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/etudiants/")
def returnEtudiants(db: Session = Depends(get_db)):
    # res = db.query(Etudiant).all()
    # return [dict(row) for row in res]
    res = (db.query(Etudiant, User.nom,User.prenom)
          .join(Etudiant, User.id_utilisateur == Etudiant.id_utilisateur)
          .all())
    return res[0]

@app.post("/users/")
async def create_user(request: Request):
    data = await request.json()
    session = Session(bind=engine)
    user = User(**data)
    session.add(user)
    session.commit()
    session.close()
    return {"message": "User added to the database"}

@app.get("/filieres/")
def returnFilieres(db: Session = Depends(get_db)):
    res = db.query(Filiere).all()
    return [dict(row) for row in res]

@app.get("/notes/{numero_etu}")
def affich_notes_etudiant(numero_etu: str, db: Session = Depends(get_db)):
    # res = db.query(Notes).join(Etudiant, Notes.id_utilisateur).filter(Etudiant.numero_etu.like({numero_etu})).all()
    # return [dict(row) for row in res]
    # query = (select([Notes.c.note])
    #      .select_from(Notes.join(Etudiant, Notes.c.id_user == Etudiant.c.id_utilisateur))
    #      .where(Etudiant.c.numero_etu == '20190821'))
    res = (db.query(Notes.note)
          .join(Etudiant, Notes.id_utilisateur == Etudiant.id_utilisateur)
          .filter(Etudiant.numero_etu == numero_etu)
          .all())
    # res = db.execute(query)
    return res[0]

@app.get("/edt/{id_filiere}")
def affich_edt_filiere(id_filiere: str, db: Session = Depends(get_db)):
    res = (db.query(Edt)
          .join(Cours, Edt.id_cours == Cours.id_cours)
          .join(Enseignant , Cours.id_enseignant == Enseignant.id_utilisateur)
          .join(Filiere, Enseignant.id_utilisateur == Filiere.id_responsable)
          .filter(Filiere.id_filiere == id_filiere)
          .all())
    return res

