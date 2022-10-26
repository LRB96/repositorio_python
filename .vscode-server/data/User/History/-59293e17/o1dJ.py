numeros_ganadores = []
for i in range(6):
    numero = int(input(f"Escribe un número ganador menor o igual a 49: "))
    try: 
        if numero <= 49:
            numeros_ganadores.append(numero)
            numeros_ganadores.sort()
    except ValueError:
        print(f"El valor ingresado no es valido.")
print(f"Los numeros ganadores son: {numeros_ganadores}.")




# numeros_ganadores = []
# for i in range(6):
#     numeros_ganadores.append(int(input("Escribe un número ganador: ")))
#     numeros_ganadores.sort()
# print(f"Los números ganadores son: {numeros_ganadores}")