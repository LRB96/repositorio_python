n = int(input("Escribe un número entero: "))
for i in range(2,n+1):
    if i % 2 != 0:
        print(f"Es primo.", {i})
    else:
        print("No es primo.")