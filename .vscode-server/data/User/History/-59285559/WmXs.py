subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))


# materias = ["Matemáticas", "Física", "Química", "Historia"]
# pasadas = []
# for materia in materias:
#     nota = float(input(f"Qué nota sacaste en {materia}: "))

