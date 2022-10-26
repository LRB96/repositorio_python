materias = ["Matemáticas", "Física", "Química", "Historia"]
notas = []
for materia in materias:
    nota = float(input(f"Qué nota sacaste en {materia}: "))
    notas.append(nota)
    if nota <= 6.0:
        notas.pop(nota)
for i in range(len(materias)):
    print(f"Debes repetir ")