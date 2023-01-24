from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = "utilisateur"
    id_utilisateur = Column(Integer, primary_key=True, index=True)
    role = Column(Integer, ForeignKey("role.id_role"))
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
    password = Column(String)
    status = Column(String)
    mail_univ = Column(String)
    tel = Column(Integer)

class Cours(Base):
    __tablename__ = "cours"
    id_cours = Column(Integer, primary_key=True, index=True)
    id_enseignant = Column(Integer, ForeignKey("enseignant.id_enseignant"))
    type_cours = Column(Enum("td", "tp", "cours", name="cours_enum"))

class Edt(Base):
    __tablename__ = "edt"
    id_edt = Column(Integer, primary_key=True, index=True)
    id_cours = Column(Integer, ForeignKey("cours.id_cours"))
    date_debut= Column(DateTime, default=datetime.utcnow)
    date_fin = Column(DateTime, default=datetime.utcnow)

class Enseignant(Base):
    __tablename__ = "enseignant"
    id_utilisateur = Column(Integer, primary_key=True, index=True)
    responsabilite_ens = Column(String)

class Etudiant(Base):
    __tablename__ = "etudiant"
    id_utilisateur = Column(Integer, primary_key=True, index=True)
    numero_etu = Column(String)
    diplome_etu = Column(String)
    diplome_etu = Column(String)
    id_filiere = Column(Integer, ForeignKey("filiere.id_filiere"))

class Filiere(Base):
    __tablename__ = "filiere"
    id_filiere = Column(Integer, primary_key=True, index=True)
    id_responsable = Column(Integer, ForeignKey("enseignant.id_utilisateur"))
    nom = Column(String)
    description = Column(String)
    niveau = Column(Enum("L", "M", "D", name="niveau_enum"))
    nombre_anne = Column(Integer)
    date_debut= Column(DateTime, default=datetime.utcnow)
    date_fin = Column(DateTime, default=datetime.utcnow)

class Horaire_enseignant(Base):
    __tablename__ = "horaire_enseignant"
    id_tache = Column(Integer, primary_key=True, index=True)
    id_utilisateur = Column(Integer, ForeignKey("enseignant.id_utilisateur"))
    nom_tache= Column(String)
    heure_tache = Column(Integer)

class Matiere(Base):
    __tablename__ = "matiere"
    id_matiere = Column(Integer, primary_key=True, index=True)
    libele_matiere = Column(String)
    description_matiere = Column(String)

class Notes(Base):
    __tablename__ = "notes"
    id_notes = Column(Integer, primary_key=True, index=True)
    id_utilisateur = Column(Integer, ForeignKey("enseignant.id_utilisateur"))
    id_cours = Column(Integer, ForeignKey("cours.id_cours"))
    note = Column(Integer)

class Role(Base):
    __tablename__ = "role"
    id_role = Column(Integer, primary_key=True, index=True)
    nom = Column(String)

class Ue(Base):
    __tablename__ = "ue"
    id_ue = Column(Integer, primary_key=True, index=True)
    id_cours = Column(Integer, ForeignKey("cours.id_cours"))
    libele_ue = Column(String)
    description_ue = Column(String)
    status = Column(String)