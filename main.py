from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base,  sessionmaker, relationship

Base = declarative_base()

# Criando classe Pai (Lado 1), (Educação- professor - Aulas)
class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    aulas = relationship("Aula", back_populates="professor")

class Aula(Base):
    __tablename__ = 'aulas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    professor = relationship("Professor", back_populates="aulas")


engine = create_engine('sqlite:///educacao.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Criando uma função para adicionar um professor
def adicionar_professor():
    with Session() as session:
        try:
            nome = input("Digite o nome do professor: ")
            professor = Professor(nome=nome)
            session.add(professor)
            session.commit()
            print(f"Professor {nome} adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar professor: {e}")
            session.rollback()

#adicionar_professor()
# Criando uma função para inserir dados da tabela Aula
def adicionar_aula():
    with Session() as session:
        try:
            titulo = input("Digite o título da aula: ")
            professor_id = int(input("Digite o ID do professor: "))
            aula = Aula(titulo=titulo, professor_id=professor_id)
            session.add(aula)
            session.commit()
            print(f"Aula {titulo} adicionada com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar aula: {e}")
            session.rollback()

adicionar_aula()
