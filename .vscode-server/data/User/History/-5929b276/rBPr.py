asignaturas = ["Matemáticas", "Inglés", "Física", "Química"]
notas = []
for asignatura in asignaturas:
    nota = input(f"Qué nota sacaste en {asignatura}")
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f"")