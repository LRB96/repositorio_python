asignaturas = ["Matemáticas", "Física", "Química", "Español", "Historia"]
notas = []
for asignatura in asignaturas:
    nota = int(input(f"¿Qué nota sacaste en {asignatura}?: "))
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f"")




# asignaturas = ["Matemáticas", "Inglés", "Física", "Química"]
# notas = []
# for asignatura in asignaturas:
#     nota = input(f"Qué nota sacaste en {asignatura}: ")
#     notas.append(nota)
# for i in range(len(asignaturas)):
#     print(f"La nota en {asignaturas[i]} es: {notas[i]}")