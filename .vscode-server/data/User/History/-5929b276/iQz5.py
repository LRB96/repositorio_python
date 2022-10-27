asignaturas = ["Matemáticas", "Inglés", "Física","Química"]
notas = []
for asignatura in asignaturas:
    nota = print(f"Que nota sacaste en {asignatura}: ")
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} la nota es: {notas[i]}.")