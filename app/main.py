from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models
from app import schemas
from app.database import SessionLocal, engine

# Cria tabelas nos PostgreSQL (se não existir)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/estudantes/', response_model=List[schemas.EstudanteResponse])
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students

@app.get('/estudantes/{id_estudante}', response_model=schemas.EstudanteResponse)
def listar_estudantes(id_estudante: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Estudante).filter(models.Estudante.id == id_estudante).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return db_student