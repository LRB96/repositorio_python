pizza = int(input("Escoge qué tipo de pizza quieres: 1. Vegetariana 2. Normal"))
ingredientes = ""
opcion_ingrediente = 0
if pizza == 1:
    opcion_ingrediente = int(input("Escoge un ingrediente: 1. Pimiento 2. Tofu."))
    print(f"Tu pizza es vegetariana y tiene Mozzarella, tomate y pimiento.")
