# Peça 1
codigo1 = str(input("Código peça 1: "))
quantidade1 = float(input("Quantidade peça 1: "))
valor1 = float(input("Valor peça 1: "))

# Peça 2
codigo2 = str(input("Código peça 2: "))
quantidade2 = float(input("Quantidade peça 2: "))
valor2 = float(input("Valor peça 2: "))


valor_pago = (quantidade1 * valor1) + (quantidade2 * valor2)

print("O valor total a ser pago é R$", valor_pago)