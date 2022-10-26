frase = input("Escribe una frase: ")
frase = frase.lower()
frase = frase.replace(" ","")
frase_invertida = frase[::-1]


print(frase_invertida)