name = input("¿Cuál es tu nombre?: ")
sex = input("¿Qué sexo eres? (M o H): ")
if sex == "M":
    if name.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if name.lower() > "n":
