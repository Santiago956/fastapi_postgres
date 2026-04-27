from sqlalchemy import \
    Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
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
    email = Column(
            String,
            unique=True,
            nullable=False
        )
    perfil = relationship(
        "Perfil",
        back_populates="estudante",
        uselist=False,
        cascade="all, delete-orphan"
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
    estudante = relationship(
        "Estudante",
        back_populates="matriculas"
    )
    nome_disciplina = Column(
        String(100),
        nullable=False
        )
    id_disciplina = Column(
        Integer,
        ForeignKey('disciplinas.id')
    )
    disciplina = relationship(
        "Disciplina",
        back_populates="matriculas"
    )

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    nome = Column(
        String(100),
        nullable=False
        )
    descricao = Column(
        String(1000),
        nullable=False
        )
    matriculas = relationship(
        "Matricula",
        back_populates="disciplina",
        cascade="all, delete-orphan"
    )


class Perfil(Base):
    __tablename__ = 'perfis'
    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    idade = Column(
        Integer,
        nullable=False
    )
    endereco = Column(
        String(100),
        nullable=False
    )
    estudante_id = Column(
        Integer,
        ForeignKey('estudantes.id'),
        unique=True,
        nullable=False
    )
    estudante = relationship(
        "Estudante",
        back_populates="perfil"
        )

class Professor(Base):
    __tablename__ = 'professores'
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    nome = Column(
        String(100),
        nullable=False
    )
    especializacao = Column(
        String(100),
        nullable=False
    )
    estudantes = relationship(
        "Estudante",
        secondary="matriculas",
        back_populates="professores"
    )
