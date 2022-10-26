from tokenize import group


name = input("¿Cuál es tu nombre?: ")
sex = input("¿Qué sexo eres? (M o H): ")
if name.lower() < "M":
    grupo = "A"
else:
    grupo = "B"
else:
    if name.lower() > "H":
        