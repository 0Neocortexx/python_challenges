from flask import *
from flask_sqlalchemy import *
import bcrypt
import os

app = Flask(__name__)
app.app_context().push()

diretorio = os.path.abspath(__file__)
path = os.path.dirname(diretorio)
arquivo = os.path.join(path, 'banco.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivo
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

# Classe normal
"""class User(object):
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Senha{self.senha}'
    
    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }
"""

class User(db.Model):
    email = db.Column(db.String(254), primary_key=True ,nullable = False)
    nome = db.Column(db.String(254), nullable = False)
    senha = db.Column(db.String(254), nullable = False)

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}'
    
    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }
    
if __name__=="__main__":
    def cripto_pass(senha):
        senha = senha.encode("utf-8")
        salt = bcrypt.gensalt(8)
        senha = bcrypt.hashpw(senha, salt)
        return senha

    def cadastrar():
        nome = str(input("Nome: ")).lower()
        email = str(input("Email: ")).lower()
        senha = str(input("Senha: "))      
        senha = cripto_pass(senha)
        pessoa = User(email = email, nome = nome, senha = senha)
        print(pessoa)
        db.session.add(pessoa)
        db.session.commit()
        print("Adicionada!")
    
    def filtro(valor:str):
        filtro = ['alert.','<script>','<','>','javascript',';','--',",","=","+",'/',"'",'"',"src=","admin'--","or 1=1", "delete from usuario", "document.write","sessionStorage.","Window.","document.",'href=',"]>", "&#34","&#39"]
        for i in filtro:
            if i not in valor:
                print(i)
            else:
                return True

    teste = filtro("&#39")
    print(teste)

