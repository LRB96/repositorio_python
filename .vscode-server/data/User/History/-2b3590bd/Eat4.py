#Crear función principal que realiza el cálculo. Con los parámetros tipo_moneda y valor_cambio.
#Crear menu que ve el usuario.
#Crear condicionales para pasar parametros a la función principal.

#En la función principal creo la variable pesos en la cual almaceno el valor que me pasa el usuario.
#Paso la variable pesos por la función float para convertirla en flotante.
#Creo la variable dolar, y le asigno pesos / valor de cambio (segundo parámetro de la función principal)
#Reasigno la variable dolar por la función round para que quede con 2 decimales después del 0.
#




def calcular(tipo_moneda, valor_cambio):
    pesos = input("¿Cuántos " + tipo_moneda + " tienes? ")
    pesos = float(pesos)
    dolar = pesos/valor_cambio
    dolar = round(dolar,2)
    dolar = str(dolar)
    print("Tienes $" + dolar + " Dólares.")

menu = """
Bienvenido al conversor de divisas.

Selecciona una:
1-Pesos Colombianos a Dólares.
2-Pesos Argentinos a Dólares.
3-Pesos Mexicanos a Dólares.
4-Dólares a Pesos Colombianos.
5-Pesos Colombianos a Euros.
6-Euros a Pesos Colombianos.
"""

opcion = int(input(menu))

if opcion == 1:
    calcular("Pesos Colombianos", 3875)
elif opcion == 2:
    calcular("Pesos Argentinos", 65)
elif opcion == 3:
    calcular("Pesos Mexicanos", 20)



elif opcion == 4:
    dolar = input("¿Cuántos Dólares tienes? ")
    dolar = float(dolar)
    valor_peso = 0.00025
    peso = dolar/valor_peso
    peso = round(peso,2)
    peso = str(peso)
    print("Tienes $" + peso + " Pesos Colombianos.")
elif opcion == 5:
    peso = input("¿Cuántos Pesos tienes? ")
    peso = float(peso)
    valor_euro = 4535
    euro = peso/valor_euro
    euro = round(euro,2)
    euro = str(euro)
    print("Tienes $" + euro + " Euros.")
elif opcion == 6:
    euro = input("¿Cuántos Euros tienes? ")
    euro = float(euro)
    valor_peso = 0.00022
    peso = euro/valor_peso
    peso = round(peso,2)
    peso = str(peso)
    print("Tienes $" + peso + " Pesos.")
else:
    print(""" Lo sorry, papi.
    Otra vez.""")