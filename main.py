print("BIENVENIDOS A LA CAMARA DEL TESORO")
print("¡Acabas de ingresar al mejor catálogo de piezas coleccionables!")

parts_inventory = []
"set para almacenar categorías únicas"
categories_set = set()

for i in range(1, 11):

    print(f"\nIngresado los datos de la pieza numero {i}")
    name = input("Ingrese su nombre: ")

    # strip() elimina espacios al inicio/final; lower() convierte el texto a minúsculas
    category = input("Ingrese la categoria de la pieza: ").strip().lower()

    price = float(input("Ingrese el precio de la pieza: "))

    status = input("Selecciona el estado de la pieza: (disponible,reservada,vendida) ").strip().lower()
    while status not in ["disponible", "reservada", "vendida"]:
        print("estatus,invalido")
        status = input("Selecciona el estado de la pieza: ")

    description = input("Ingrese la descripcion de la pieza (Usada,Certificada)  ").strip().lower()
    while description not in ["usada", "certificada"]:
        print("descripcion,invalido")
        description = input("descripcion invalido: ")

    parts = {
        "id": i,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

    parts_inventory.append(parts)
    categories_set.add(category)

    print("Registro exitoso")

selected_view = input("\n1. Ver todas las piezas / 2. Ver una pieza individual / 3. Ver categorías: ")

if selected_view == "1":
    print("Catalogo completo")
    print("\n")
    for item in parts_inventory:
        print(f"Identificador: {item['id']}")
        print(f"Nombre: {item['name']}")
        print(f"Categoría: {item['category']}")
        print(f"Precio: ${item['price']}")
        print(f"Estado: {item['status']}")
        print(f"Descripción: {item['description']}")
        print("\n")

    print("Informe general de todas las piezas")
    print(f"Total de piezas registradas: {len(parts_inventory)}")

elif selected_view == "2":
    item_position = int(input(f"Ingrese la posicion del pieza (1 al {len(parts_inventory)}): "))

    if 1 <= item_position <= len(parts_inventory):
        index = item_position - 1
        print("Detalles del pieza:")
        print(parts_inventory[index])
    else:
        print("Posicion fuera del rango")

elif selected_view == "3":
    print("\nCategorias registradas:")
    print(f"Categorías únicas: {categories_set}")
    print(f"Total de categorías diferentes: {len(categories_set)}")

else:
    print("Opcion invalido")
