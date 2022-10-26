def es_palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_inversa = palabra[::-1]
    if palabra_inversa == palabra:
        True
    else:
        False



def run():
    palabra = input("Escribe una palabra o frase: ")
    if es_palindromo:
        print("Es un palindromo.")
    else:
        print("No es un palindromo.")



if __name__ == "__main__":
    run()