renta = float(input("'¿Cuánto ganas al año?: "))
if renta < 10000:
    tipo_impositivo = 5
elif renta >= 10000 or renta <= 20000:
    tipo_impositivo = 15
elif renta 