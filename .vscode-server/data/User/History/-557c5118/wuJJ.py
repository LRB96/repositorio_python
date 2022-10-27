cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Tasa de interés: "))
anios = int(input("Años a invertir: "))
for i in range(anios):
    monto = monto * (1 + interes) ** anios
    if i == 1:
        print(f"La cantidad de dinero después de {i+1} es de: {monto}")
    else: 
        print(f"La cantidad de dinero después de {i +1} es de: {monto}")