print("BIENVENIDOS A LA CAMARA DEL TESORO")
print("¡Acabas de ingresar al mejor catálogo de piezas coleccionables!")

parts_inventory = []
categories_set = set()

for i in range(1, 11):

    print(f"\nIngresando los datos de la pieza número {i}")
    name = input("Ingrese su nombre: ")

    category = input("Ingrese la categoría de la pieza: ").strip().lower()

    while True:
        try:
            price = float(input("Ingrese el precio de la pieza: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    status = input("Selecciona el estado de la pieza: (disponible, reservada, vendida) ").strip().lower()
    while status not in ["disponible", "reservada", "vendida"]:
        print("Estatus inválido")
        status = input("Selecciona el estado de la pieza: ").strip().lower()

    description = input("Ingrese la descripción de la pieza (usada, certificada): ").strip().lower()
    while description not in ["usada", "certificada"]:
        print("Descripción inválida")
        description = input("Ingrese la descripción de la pieza: ").strip().lower()

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


while True:
    print("\n" + "=" * 50)
    print("      MENÚ PRINCIPAL - CÁMARA DEL TESORO")
    print("=" * 50)
    print("1. Ver todas las piezas")
    print("2. Ver una pieza individual")
    print("3. Ver categorías")
    print("4. Filtrar por estado")
    print("5. Filtrar por precio mínimo")
    print("6. Ver precio promedio del catálogo")
    print("7. Evaluar reglas del catálogo")
    print("8. Manipulación de strings")
    print("9. Salir del programa")

    selected_view = input("\nSeleccione una opción (1-9): ").strip()

    if selected_view == "1":
        print("\nCatálogo completo\n")
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
        while True:
            try:
                item_position = int(input(f"\nIngrese la posición de la pieza (1 al {len(parts_inventory)}): "))
                break
            except ValueError:
                print("Error: Ingrese un número entero válido.")

        if 1 <= item_position <= len(parts_inventory):
            index = item_position - 1
            print("\nDetalles de la pieza:")
            print(parts_inventory[index])
        else:
            print("Posición fuera del rango")

    elif selected_view == "3":
        print("\nCategorías registradas:")
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

    elif selected_view == "6":
        print("\nPRECIO PROMEDIO DEL CATÁLOGO")
        if len(parts_inventory) > 0:
            total_sum = sum(item["price"] for item in parts_inventory)
            average_price = total_sum / len(parts_inventory)
            print(f"El precio promedio de las piezas es: ${average_price:.2f}")
        else:
            print("No hay piezas en el catálogo para calcular el promedio.")

    elif selected_view == "7":
        print("\nEVALUACIÓN DE REGLAS LÓGICAS")

        print("\nRegla de Publicación (Precio > 0 y Disponible)")
        for item in parts_inventory:
            can_publish = item["price"] > 0 and item["status"] == "disponible"
            status_text = "SÍ puede publicarse" if can_publish else "NO puede publicarse"
            print(f"ID: {item['id']} | Nombre: {item['name']} -> {status_text}")

        print("\nRegla de Revisión (Reservada o Vendida)")
        for item in parts_inventory:
            needs_review = item["status"] == "reservada" or item["status"] == "vendida"
            review_text = "SÍ requiere revisión" if needs_review else "NO requiere revisión"
            print(f"ID: {item['id']} | Nombre: {item['name']} -> {review_text}")

        print("\nPiezas No Vendidas")
        found_not_sold = False
        for item in parts_inventory:
            if item["status"] != "vendida":
                print(
                    f"ID: {item['id']} | Nombre: {item['name']} | Estado: {item['status']} | Precio: ${item['price']}")
                found_not_sold = True

        if not found_not_sold:
            print("Todas las piezas registradas se encuentran vendidas.")

    elif selected_view == "8":
        print("\nMANIPULACIÓN DE STRINGS")

        if len(parts_inventory) > 0:
            sample_item = parts_inventory[0]

            print("\nConcatenación")
            concatenated_info = "Pieza: " + sample_item["name"] + " | Categoría: " + sample_item[
                "category"] + " | Precio: $" + str(sample_item["price"])
            print(concatenated_info)

            print("\nInterpolación")
            interpolated_info = f"Pieza: {sample_item['name']} | Categoría: {sample_item['category']} | Precio: ${sample_item['price']}"
            print(interpolated_info)

            print("\nReemplazo de texto")
            original_desc = sample_item["description"]
            updated_desc = original_desc.replace("usada", "certificada")
            print(f"Descripción original: {original_desc}")
            print(f"Descripción modificada: {updated_desc}")
        else:
            print("\nNo hay piezas en el inventario para mostrar ejemplos.")

        print("\nConversión de etiquetas")
        raw_tags = input("Ingrese etiquetas para la pieza separadas por comas (ej. rara,antigua,edicion_limitada): ")
        tags_list = [tag.strip() for tag in raw_tags.split(",")]
        print(f"Lista de etiquetas procesadas: {tags_list}")

        print("\nFormato de nombre de usuario")
        username_input = input("Ingrese su nombre de usuario: ")
        print(f"Sin espacios al inicio/final: '{username_input.strip()}'")
        print(f"En minúsculas: '{username_input.strip().lower()}'")
        print(f"En mayúsculas: '{username_input.strip().upper()}'")

    elif selected_view == "9":
        print("\n¡Gracias por utilizar el catálogo de la Cámara del Tesoro! Hasta pronto.")
        break

    else:
        print("\nOpción inválida. Por favor, ingrese un número del 1 al 10.")