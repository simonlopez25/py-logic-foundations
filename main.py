print("BIENVENIDOS A LA CAMARA DEL TESORO")
print("¡Acabas de ingresar al mejor catálogo de piezas coleccionables!")

parts_inventory = []
categories_set = set()

for i in range(1, 2):

    print(f"\nIngresado los datos de la pieza numero {i}")
    name = input("Ingrese su nombre: ")

    category = input("Ingrese la categoria de la pieza: ").strip().lower()

    # Validación de precio con while True
    while True:
        try:
            price = float(input("Ingrese el precio de la pieza: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    status = input("Selecciona el estado de la pieza: (disponible,reservada,vendida) ").strip().lower()
    while status not in ["disponible", "reservada", "vendida"]:
        print("estatus invalido")
        status = input("Selecciona el estado de la pieza: ").strip().lower()

    description = input("Ingrese la descripcion de la pieza (Usada,Certificada): ").strip().lower()
    while description not in ["usada", "certificada"]:
        print("descripcion invalida")
        description = input("Ingrese la descripcion de la pieza: ").strip().lower()

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

selected_view = input(
    "\n1. Ver todas las piezas / 2. Ver una pieza individual / 3. Ver categorías / 4. Filtrar por estado / 5. Filtrar por precio mínimo: ")

if selected_view == "1":
    print("Catalogo completo\n")
    for item in parts_inventory:
        print(f"Identificador: {item['id']}")
        print(f"Nombre: {item['name']}")
        print(f"Categoría: {item['category']}")
        print(f"Precio: ${item['price']}")
        print(f"Estado: {item['status']}")
        print(f"Descripción: {item['description']}\n")

    print("Informe general de todas las piezas")
    print(f"Total de piezas registradas: {len(parts_inventory)}")

elif selected_view == "2":
    item_position = int(input(f"Ingrese la posicion de la pieza (1 al {len(parts_inventory)}): "))

    if 1 <= item_position <= len(parts_inventory):
        index = item_position - 1
        print("Detalles de la pieza:")
        print(parts_inventory[index])
    else:
        print("Posicion fuera del rango")

elif selected_view == "3":
    print("\nCategorias registradas:")
    print(f"Categorías únicas: {categories_set}")
    print(f"Total de categorías diferentes: {len(categories_set)}")

elif selected_view == "4":
    print("\nPiezas disponibles")
    status_available = False
    for item in parts_inventory:
        if item["status"] == "disponible":
            print(f"ID: {item['id']} | Nombre: {item['name']} | Precio: ${item['price']}")
            status_available = True
    if not status_available:
        print("No hay piezas disponibles")

    print("\nPiezas reservadas")
    status_reserved = False
    for item in parts_inventory:
        if item["status"] == "reservada":
            print(f"ID: {item['id']} | Nombre: {item['name']} | Precio: ${item['price']}")
            status_reserved = True
    if not status_reserved:
        print("No hay piezas reservadas")

    print("\nPiezas vendidas")
    status_sold = False
    for item in parts_inventory:
        if item["status"] == "vendida":
            print(f"ID: {item['id']} | Nombre: {item['name']} | Precio: ${item['price']}")
            status_sold = True
    if not status_sold:
        print("No hay piezas vendidas")

elif selected_view == "5":
    print("\nFiltrar por precio mínimo")

    while True:
        try:
            min_price = float(input("Ingrese el precio mínimo: "))
            break
        except ValueError:
            print("Ingrese un valor válido (números).")

    print(f"\nPiezas con precio superior a ${min_price}:")
    found_items = False
    for item in parts_inventory:
        if item["price"] > min_price:
            print(
                f"ID: {item['id']} | Nombre: {item['name']} | Categoría: {item['category']} | Precio: ${item['price']}")
            found_items = True

    if not found_items:
        print(f"No se encontraron piezas con un precio superior a ${min_price}")

else:
    print("Opcion invalida")