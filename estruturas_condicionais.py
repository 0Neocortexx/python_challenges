codigo = int(input("Código: "))
quantidade = float(input("Quantidade: "))

if codigo == 1:
    valor_final = quantidade * 4
    print("Tota: R$",valor_final)
elif codigo == 2:
    valor_final = quantidade * 4.50
    print("Tota: R$",valor_final)
elif codigo == 3:
    valor_final = quantidade * 5
    print("Tota: R$",valor_final)
elif codigo == 4:
    valor_final = quantidade * 2
    print("Tota: R$",valor_final)
elif codigo == 5:
    valor_final = quantidade * 1.50
    print("Tota: R$",valor_final)
else:
    print("Código invalido!")