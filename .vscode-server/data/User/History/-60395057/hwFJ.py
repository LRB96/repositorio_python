import sys
import time

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


def fibonacci_dinamico(n, memo={}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except:
        resultado = fibonacci_dinamico(n-1,memo) + fibonacci_dinamico(n-2, memo)
        memo[n] = resultado

        return resultado




if __name__ == "__main__":
    sys.setrecursionlimit(1000002)
    n = int(input("Escribe un número:"))
    resultado = fibonacci_dinamico(n)
    print(resultado)
    tiempo = time.time()
    print(tiempo)