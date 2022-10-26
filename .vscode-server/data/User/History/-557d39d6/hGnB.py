num = int(input("Escribe un número entero: "))

for i in range(1, num+1, 2):
        print(f"Los números impares desde 1 hasta {num}.")
        print(i, end=",")