from pydantic import BaseModel, Field

class EstudanteBase(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    idade: int = Field(gt=15, lt=100)

class EstudanteCreate(EstudanteBase):
    pass

class EstudanteResponse(EstudanteBase):
    id: int
    class Config:
        from_attributes = True
    
class MatriculaBase(BaseModel):
    id_estudante: int
    nome_disciplina: str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int
    class Config:
        from_attributes = True

