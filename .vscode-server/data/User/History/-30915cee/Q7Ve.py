interes = 0.04
ahorros = float(input("¿Cuántos ahorros quieres meter en tu cuenta?: "))

balance1 = ahorros * (1+interes) 
print(f"Tus ahorros el primer año son de: {balance1}.")

balance2 = balance1 * (1+interes)
print(f"Tus ahorros el segundo año son de: {balance2}.")

balance3 = balance2 * (1+interes)
print(f"Tus ahorros el tercer año son de: {balance3}.")