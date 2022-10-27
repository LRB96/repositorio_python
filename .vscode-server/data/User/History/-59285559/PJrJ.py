materias = ["Matemáticas", "Física", "Química", "Historia"]
for i in range(len(materias)-1,-1,-1):
    nota = float(input(f"Qué nota sacaste en {materias[i]}: "))
    if nota >= 5:
        materias.pop(i)
    print(f"Debes repetir {materias}.")