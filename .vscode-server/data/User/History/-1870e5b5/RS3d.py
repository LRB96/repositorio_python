pizza = int(input("Escoge qué tipo de pizza quieres: 1. Vegetariana 2. Normal"))
ingredientes = ""
opcion_ingrediente = 0

if pizza == 1:
    opcion_ingrediente = int(input("Escoge un ingrediente: 1. Pimiento 2. Tofu."))
    if opcion_ingrediente == 1:
        print(f"Tu pizza es vegetariana y tiene Mozzarella, tomate y pimiento.")
    elif opcion_ingrediente == 2:
        print("Tu pizza es vegetariana y tiene Mozzarella, tomate y tofu.")
    else:
        print("Opción incorrecta.")

if pizza == 2:
    opcion_ingrediente =int(input("Escoge un ingrediente: 1. Peperoni 2. jamón 3. salmón"))
    if opcion_ingrediente == 1:
        