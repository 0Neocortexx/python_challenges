senha = "2002"
while True:
    tentativa = str(input("Digite a senha: "))
    if tentativa == senha:
        print("Acesso Permitido!")
        break
    else:
        print("Senha inválida!")