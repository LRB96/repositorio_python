import time

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)






if __name__ == "__main__":
    n = int(input("Escribe un número:"))
    resultado = fibonacci_recursivo(n)
    print(resultado)
    tiempo = time.time()
    print(tiempo)