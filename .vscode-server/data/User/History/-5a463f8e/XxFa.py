n = int(input("Escribe un número entero: "))
for i in range(2,n+1):
    if i % 2 != 0:
        print("Es primo.")
    else:
        print("No es primo.")