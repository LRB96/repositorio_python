precio = input("Introduce el precio del producto con 2 decimales: ")
print(f"El precio es de {precio[:precio.find(".")]} con {precio[precio.find(".")+1:]} céntavos.")