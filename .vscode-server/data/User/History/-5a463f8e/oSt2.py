n = int(input("Escribe un número entero: "))
for i in range(2,n+1):
    if n % i != 0:
        break
if 