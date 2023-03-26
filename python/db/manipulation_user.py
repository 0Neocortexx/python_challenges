from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import bcrypt

app = Flask(__name__)
app.app_context().push()

# caminho do banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'teste.db')

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Usuario(db.Model):
    email = db.Column(db.String(254), primary_key=True, nullable=False)
    nome = db.Column(db.String(254), nullable=False)
    senha = db.Column(db.String(254), nullable=False)

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}'

    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }
if __name__=="__main__":
  def cadastrar_pessoa():
      nome = str(input("NOME: "))
      email = str(input("EMAIL:"))
      senha = str(input("SENHA: "))
      senha = cript(senha)
      user = Usuario(nome = nome, email = email , senha = senha)
      db.session.add(user)
      db.session.commit()

  def cript(senha):
      senha = senha("utf-8")
      senha = bcrypt.hashpw()
      print(senha)
  """  # db.create_all()
    usuario = Usuario(nome = "Alan", email= "Alan123@gmail.com", senha = "Alan123")
    print("ADICIONADO!")
    db.session.add(usuario)
    db.session.commit()"""
  cadastrar_pessoa()