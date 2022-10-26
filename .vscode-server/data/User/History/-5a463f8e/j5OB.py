n = int(input("Escribe un número entero: "))
i = 2
while n % i != 0:
    i += 1
# for i in range(2,n+1):
if i % 2 != 0:
    print(f"{i} es primo.")
else:
    print(f"{i} no es primo.")