from sqlalchemy import create_engine

# Conectar a SQLite em memoria
engine =  create_engine('sqlite:///meubanco.db', echo=True)

print('COnexão com banco estabelecida')

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__='usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar tabela no banco de dados

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# novo_usuario = Usuario(nome='Joao', idade=28)
# session.add(novo_usuario)
# session.commit()

# print('Usuario inserido com sucesso')

# usuario = session.query(Usuario).filter_by(nome='Ana').first()
# print(f"Usuario encontrado {usuario.nome}, Idade: {usuario.idade}")

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()
