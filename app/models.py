from sqlalchemy import \
    Column, Integer, String, ForeignKey
from app.database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(
            Integer,
            primary_key=True,
            index=True
        )
    nome = Column(
            String(100),
            nullable=False
        )
    idade = Column(
            Integer
        )

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    id_estudante = Column(
        Integer,
        ForeignKey('estudantes.id')
        )
    nome_disciplina = Column(
        String(100),
        nullable=False
        )
    