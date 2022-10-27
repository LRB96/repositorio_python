import time



def fibo_gen(number: int) -> int:
    n1 = 0
    n2 = 1
    counter = 0
    while number:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux



def run():
    number: int = int(input("Escribe un número máximo para la secuencia de Fibonacci: "))
    fibonacci = fibo_gen(number)
    for element in fibonacci:
        print(element)
        time.sleep(1)



if __name__ == "__main__":
    run()