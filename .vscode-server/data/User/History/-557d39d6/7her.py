num = int(input("Escribe un número entero: "))

if num % 3 == 0:
    for i in range(num):
        print(f"Los números impares desde 1 hasta {num} son: {i}")