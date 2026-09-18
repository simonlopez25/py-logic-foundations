print("BIENVENIDOS A LA CAMARA DEL TESORO")
print("¡Acabas de ingresar al mejor catálogo de piezas coleccionables!")

parts_inventory = []

for i in range(1,2):

    print(f"\nIngresado los datos de la pieza numero {i}")
    name = input("Ingrese su nombre: ")
    category = input("Ingrese la categoria de la pieza: ")
    price = float(input("Ingrese el precio de la pieza: "))

    status = input("Selecciona el estado de la pieza: (Disponible,Reservada,Vendida) ")
    while status not in ["Disponible", "Reservada", "Vendida"]:
        print("Estatus invalido")
        status = input("Selecciona el estado de la pieza: ")

    description = input("Ingrese la descripcion de la pieza (Usada,Certificada)  ")
    while description not in ["Usada", "Certificada"]:
        status = input("Descripcion invalido: ")

    parts = {
        "id": i,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }
    "APPEND ME SIRVE PARA REGISTRAR CORRECTAMENTE LOS DATOS"
    parts_inventory.append(parts)

    print("Registro exitoso")
    print(f"Se han registrado {len(parts_inventory)} piezas")


