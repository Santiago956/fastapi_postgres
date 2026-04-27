from pydantic import BaseModel, Field
from typing import List, Optional

class Estudante(BaseModel):
    id: int
    nome: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=3, max_length=100)
    perfil: Optional['Perfil'] = None

    class Config:
        from_attributes = True


class PerfilCreate(BaseModel):
    idade: int = Field(gt=15, lt=100)
    endereco: str = Field(max_length=100)


class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate

class PerfilUpdate(BaseModel):
    idade: Optional[int] = Field(None, gt=15, lt=100)
    endereco: Optional[str] = Field(None, max_length=100)

class EstudanteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    perfil: Optional[PerfilUpdate] = None

class Perfil(BaseModel):
    id: int
    idade: int = Field(gt=15, lt=100)
    endereco: str = Field(max_length=100)

    class Config:
        from_attributes = True


class Disciplina(BaseModel):
    id: int
    nome: str
    descricao: str = Field(max_length=1000)

    class Config:
        from_attributes = True

class DisciplinaCreate(BaseModel):
    nome: str
    descricao: str = Field(max_length=1000)
    
class MatriculaBase(BaseModel):
    id_estudante: int
    nome_disciplina: str

    class Config:
        from_attributes = True

class MatriculaCreate(MatriculaBase):
    id_estudante: int
    id_disciplina: int

class MatriculaResponse(MatriculaBase):
    id: int
    class Config:
        from_attributes = True

class Professor(BaseModel):
    nome: str
    especializacao: str

    class Config:
        from_attributes = True
    
class ProfessorCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    especializacao: str = Field(min_length=3, max_length=100)



