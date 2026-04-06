from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base,  sessionmaker, relationship

Base = declarative_base()

# Criando classe Pai (Lado 1), (Educação- professor - Aulas)
class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    aulas = relationship("Aula", back_populates="professor")
    horario = relationship("Horario", back_populates="professor", uselist=False)

class Aula(Base):
    __tablename__ = 'aulas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    professor = relationship("Professor", back_populates="aulas")
