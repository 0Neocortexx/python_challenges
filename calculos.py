# Pegar o maior e menor numero de uma lista
def maior_e_menor(num1:float, num2:float, num3:float):
    numeros = [num1, num2, num3]
    print("Numeros: ", numeros)
    print("Maior numero", max(numeros))
    print("Menor numero", min(numeros))
# maior_e_menor(20,12,5)

# Calcular área de um circulo
def calcular_area_circulo(raio:str):
    calculo = (3.14*(raio**2))
    print("A área do circulo é:", calculo)
# calcular_area_circulo(2)

# Gerador de tabuada
def tabuada():
    numero = float(input("Qual tabuada você deseja: "))
    for i in range(1,11):
        print(numero ,"x", i, "=", i * numero)
# tabuada()

# Calcular o numero possivel de faltas
def numero_de_faltas_possiveis():
    meses = int(input("Quantos meses duram o curso? "))
    porcentagem_de_falta = float(input("Qual a porcetagem de presença minima permitida? "))
    semanas = meses * 4
    condicao = str(input("O sabado é um dia letivo? (S) or (N): "))
    if condicao == "S":
        aulas = semanas * 6
        porcentagem_de_falta = porcentagem_de_falta / 100
        faltas = (aulas * porcentagem_de_falta)
        possiveis_faltas = aulas - faltas
        print("Aulas", aulas)
        print("Presenças", faltas)
        print("Possiveis faltas", possiveis_faltas)
    elif condicao == "N":
        aulas = semanas * 5
        porcentagem_de_falta = porcentagem_de_falta / 100
        faltas = (aulas * porcentagem_de_falta)
        possiveis_faltas = aulas - faltas
        print("Aulas", aulas)
        print("Presenças", faltas)
        print("Possiveis faltas", possiveis_faltas)
    else:
        print("Digite um valor válido!")
# numero_de_faltas_possiveis()
