print("BIENVENIDOS A LA CAMARA DEL TESORO")
print("¡Acabas de ingresar al mejor catálogo de piezas coleccionables!")

parts_inventory = []

for i in range(1, 2):

    print(f"\nIngresado los datos de la pieza numero {i}")
    name = input("Ingrese su nombre: ")
    category = input("Ingrese la categoria de la pieza: ")
    price = float(input("Ingrese el precio de la pieza: "))

    status = input("Selecciona el estado de la pieza: (disponible,reservada,vendida) ")
    while status not in ["disponible", "reservada", "vendida"]:
        print("estatus,invalido")
        status = input("Selecciona el estado de la pieza: ")

    description = input("Ingrese la descripcion de la pieza (Usada,Certificada)  ")
    while description not in ["usada", "certificada"]:
        print("descripcion,invalido")
        description = input("descripcion invalido digita la descripcion estipulada: ")

    parts = {
        "id": i,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

    parts_inventory.append(parts)
    print("Registro exitoso")

selected_view = input("\n1. Ver todas las piezas / 2. Ver una pieza individual: ")

if selected_view == "1":
    print("Catalogo completo")
    for item in parts_inventory:
        print(item)

elif selected_view == "2":
    item_position = int(input(f"Ingrese la posicion del pieza (1 al {len(parts_inventory)}): "))

    if 1 <= item_position <= len(parts_inventory):
        index = item_position - 1
        print("Detalles del pieza:")
        print(parts_inventory[index])
    else:
        print("Posicion fuera del rango")
else:
    print("Opcion invalido")