import bcrypt

# Contar letras de palavras de uma frase
def contador_de_letras(frase:str):
    palavra1 = frase[:6]
    palavra2 = frase[7:9]
    palavra3 = frase[10:14]
    palavra4 = frase[15:19]
    print("Palavra 1 = ", palavra1, ".", "A palavra possui ", len(palavra1), "letras!")
    print("Palavra 2 = ", palavra2, ".", "A palavra possui ", len(palavra2), "letras!")
    print("Palavra 3 = ", palavra3, ".", "A palavra possui ", len(palavra3), "letras!")
    print("Palavra 4 = ", palavra4, ".", "A palavra possui ", len(palavra4), "letras!")
# contador_de_letras("Python is very nice")

# -------------------------------

# Inverter palavra 
def inverter_palavra(palavra:str):
    print("Seu inverso é", palavra[::-1])
# inverter_palavra("Pneumotramicroscopicosilicovulcanoconiotico")

# -------------------------------

# Deixar texto em minusculo
def minusculo(palavra):
    palavra = palavra.lower()
    return palavra 
# palavra = minusculo("PALAVRA")
# print(palavra)

# -------------------------------

# Deixar texto em maiusculo
def minusculo(palavra):
    palavra = palavra.upper()
    return palavra 
# palavra = minusculo("palavra")
# print(palavra)

# -------------------------------

# Hello apple pie
# No words
def imprimit_repetidas(frase:str):
    frase = frase.split()
    for i in frase:
        letras = len(i)
    print(letras)
# imprimit_repetidas("Hello apple pie")

# -------------------------------

def cript_in_sha256():
    import json
    import hashlib
    dicionario1 = '{ "nome" : "Alan","usuario" : "Alan Souza","senha" : "Alan@123"}'
    dicionario2 = {
        "nome" : "Pedro",
        "usuario" : "Pedro Barbosa",
        "senha" : "Pedro@0123"
    }
    pesquisa = json.loads(dicionario1)
    senha = pesquisa["senha"]
    senha = hashlib.sha256()
    print(senha)

# -------------------------------

def resgatar_informacao_do_json():
    import json
    import bcrypt
    dicionario1 = '{ "nome" : "Alan","usuario" : "Alan Souza","senha" : "Alan@123"}'
    dicionario2 = {
    "nome": "Pedro",
    "usuario": "Pedro Barbosa",
    "senha": "Pedro@0123"
    }
    pesquisa = json.loads(dicionario1)
    senha = pesquisa["senha"]
    user = pesquisa["usuario"]

# -------------------------------

def tratar_user(usuario: str):
   usuario = usuario.lower()
   # Replace troca um item de uma string por outro, por exemplo um espaço por vazio e junta
   usuario = usuario.replace(" ", "")
   return usuario

# -------------------------------

def tratar_senha(senha:str):
    hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt(8))
    return hashed
    user_tratado = tratar_user(user)
    # print(user_tratado)
    senha_tratada = tratar_senha(senha)
    # print(senha_tratada)
    user = []
    user.append(user_tratado)
    user.append(senha_tratada)
    # print(user)
    senhas = []
    senhas.append(senha_tratada)
    # print(senhas)

    
def conferir(senha:str, lista:list) -> bool:
   if senha not in lista:
       return False
   else:
       return True
#confere = conferir(senha, senhas)

# print(confere)
# tratar_user(user)
# print(user)
# print(senha)
