from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models
from app import schemas
from sqlalchemy.orm import joinedload
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


# ==========================================
# ESTUDANTES
# ==========================================

@app.post('/estudantes/', response_model=schemas.Estudante)
def create_student(student: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_student = models.Estudante(
        nome=student.nome,
        email=student.email,
        perfil=models.Perfil(**student.perfil.dict())
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/estudantes/', response_model=List[schemas.Estudante])
def list_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()
    return students

@app.get('/estudantes/{id_estudante}', response_model=schemas.Estudante)
def list_student_by_id(id_estudante: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).filter(models.Estudante.id == id_estudante).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return db_student

@app.patch('/estudantes/{id_estudante}')
def update_student(id_estudante: int, student: schemas.EstudanteUpdate, db: Session = Depends(get_db)):
    db_student = db.query(models.Estudante).filter(models.Estudante.id == id_estudante).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    
    update_data = student.model_dump(exclude_unset=True)
    
    if "perfil" in update_data:
        perfil_data = update_data.pop("perfil")
        if db_student.perfil:
            for key, value in perfil_data.items():
                setattr(db_student.perfil, key, value)
        else:
            db_student.perfil = models.Perfil(**perfil_data)

    for key, value in update_data.items():
        setattr(db_student, key, value)
        
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete('/estudantes/{id_estudante}')
def delete_student(id_estudante: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Estudante).filter(models.Estudante.id == id_estudante).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    db.delete(db_student)
    db.commit()
    return {"message": "Estudante deletado com sucesso"}


# ==========================================
# PROFESSORES
# ==========================================

@app.post('/professores/', response_model=schemas.Professor)
def create_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_professor = models.Professor(
        nome=professor.nome,
        especializacao=professor.especializacao
    )
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.get('/professores/', response_model=List[schemas.Professor])
def list_professors(db: Session = Depends(get_db)):
    professors = db.query(models.Professor).all()
    return professors

@app.get('/professores/{id_professor}', response_model=schemas.Professor)
def list_professor_by_id(id_professor: int, db: Session = Depends(get_db)):
    db_professor = db.query(models.Professor).filter(models.Professor.id == id_professor).first()
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return db_professor

@app.patch('/professores/{id_professor}')
def update_professor(id_professor: int, professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_professor = db.query(models.Professor).filter(models.Professor.id == id_professor).first()
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    update_data = professor.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_professor, key, value)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.delete('/professores/{id_professor}')
def delete_professor(id_professor: int, db: Session = Depends(get_db)):
    db_professor = db.query(models.Professor).filter(models.Professor.id == id_professor).first()
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    db.delete(db_professor)
    db.commit()
    return {"message": "Professor deletado com sucesso"}


# ==========================================
# DISCIPLINAS
# ==========================================

@app.post('/disciplinas/', response_model=schemas.Disciplina)
def create_discipline(discipline: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    db_discipline = models.Disciplina(
        nome=discipline.nome,
        descricao=discipline.descricao
    )
    db.add(db_discipline)
    db.commit()
    db.refresh(db_discipline)
    return db_discipline

@app.get('/disciplinas/', response_model=List[schemas.Disciplina])
def list_disciplines(db: Session = Depends(get_db)):
    disciplines = db.query(models.Disciplina).all()
    return disciplines

@app.get('/disciplinas/{id_disciplina}', response_model=schemas.Disciplina)
def list_discipline_by_id(id_disciplina: int, db: Session = Depends(get_db)):
    db_discipline = db.query(models.Disciplina).filter(models.Disciplina.id == id_disciplina).first()
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return db_discipline

@app.patch('/disciplinas/{id_disciplina}')
def update_discipline(id_disciplina: int, discipline: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    db_discipline = db.query(models.Disciplina).filter(models.Disciplina.id == id_disciplina).first()
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    update_data = discipline.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_discipline, key, value)
    db.commit()
    db.refresh(db_discipline)
    return db_discipline

@app.delete('/disciplinas/{id_disciplina}')
def delete_discipline(id_disciplina: int, db: Session = Depends(get_db)):
    db_discipline = db.query(models.Disciplina).filter(models.Disciplina.id == id_disciplina).first()
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    db.delete(db_discipline)
    db.commit()
    return {"message": "Disciplina deletada com sucesso"}
