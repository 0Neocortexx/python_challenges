a = float(input("Valor A: "))
b = float(input("Valor B: "))
c = float(input("Valor C: "))
delta = (b**2)- (4*a*c)

if a != 0 and delta >= 0:
    x1 = ((-b + (delta**0.5))/(2*a))
    x2 = ((-b - (delta**0.5))/(2*a))
    x1 = "{:.5f}".format(x1)
    x2 = "{:.5f}".format(x2)
    print("X1:",x1," X2:",x2)
else:
    print("Impossivel Calcular!")