from colorama import AnsiToWin32

cantidad = float(input("¿Cuánto quieres invertir?: "))
interes = float(input("¿A cuánto intrerés porcentual anual?: "))
annos = int(input("¿A cuántos años?: "))

print(f"El capital final es de: {cantidad * (interes /100 +1) ** annos}.") 