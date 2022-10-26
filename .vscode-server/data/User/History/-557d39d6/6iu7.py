from re import I


num = I(input("Escribe un número entero: "))

for i in range(num):
    if num % 3 == 0:
        print(f"Los números impares desde 1 hasta {num} son: {i}")