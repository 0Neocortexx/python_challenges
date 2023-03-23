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

# Inverter palavra 
def inverter_palavra(palavra:str):
    print("Seu inverso é", palavra[::-1])
# inverter_palavra("Pneumotramicroscopicosilicovulcanoconiotico")

# Deixar texto em minusculo
def minusculo(palavra):
    palavra = palavra.lower()
    return palavra 
# palavra = minusculo("PALAVRA")
# print(palavra)

# Deixar texto em maiusculo
def minusculo(palavra):
    palavra = palavra.upper()
    return palavra 
# palavra = minusculo("palavra")
# print(palavra)