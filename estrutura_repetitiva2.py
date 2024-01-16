n = int(input("Digite a quantidade de valores: "))
valores = []
for i in range(0,n):
    num = int(input(("Valor: ")))
    valores.append(num)
print(valores)

count = 0
for a in valores:
    if a in [10,11,12,13,14,15,16,17,18,19,20]:
        count = count + 1
print(count,"in", n - count, "out")