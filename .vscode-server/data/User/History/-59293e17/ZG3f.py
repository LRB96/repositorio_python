numeros_ganadores = []
for i in range(6):
    numero = (int(input("Escribe un número ganador: ")))
    if numero >= 49:
        numeros_ganadores.append(i)
        numeros_ganadores.sort()
    else:
        numeros_ganadores.pop(i*1)
print(f"Los numeros ganadores son: {numeros_ganadores}.")




# numeros_ganadores = []
# for i in range(6):
#     numeros_ganadores.append(int(input("Escribe un número ganador: ")))
#     numeros_ganadores.sort()
# print(f"Los números ganadores son: {numeros_ganadores}")