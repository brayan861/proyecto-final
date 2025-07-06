inventario = {
    'chamarras': {'cantidad': 350, 'precio': 180.00},
    'zapatos': {'cantidad': 200, 'precio': 130.00},
    'mochilas': {'cantidad': 310, 'precio': 125.00}
}

while True:
    print("\n--- Sistema de Control de Productos ---")
    print("1. Añadir Nuevos Productos")
    print("2. Modificar Stock actual")
    print("3. Quitar Productos del Inventario")
    print("4. Mostrar Lista de Productos")
    print("5. Buscar en el Inventario")
    print("6. Ver Estado del Inventario")
    print("7. Finalizar Programa")
    print("----------------------------------------")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("\n--- Añadir Nuevos Productos ---")
        nombre_producto = input("Ingrese el nombre del producto: ").strip().capitalize()
        if nombre_producto in inventario:
            print(f"Error: El producto '{nombre_producto}' ya existe en el inventario.")
        else:
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad inicial: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")
            while True:
                try:
                    precio = float(input("Ingrese el precio unitario (mínimo 50): "))
                    if precio < 50:
                        print("El precio debe ser igual o mayor a 50. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número para el precio.")
            inventario[nombre_producto] = {'cantidad': cantidad, 'precio': precio}
            print(f"Producto '{nombre_producto}' añadido exitosamente.")

    elif opcion == '2':
        print("\n--- Modificar Stock Existente ---")
        nombre_a_actualizar = input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
        if nombre_a_actualizar not in inventario:
            print(f"Error: El producto '{nombre_a_actualizar}' no se encuentra en el inventario.")
        else:
            print(f"Producto '{nombre_a_actualizar}' encontrado. Cantidad actual: {inventario[nombre_a_actualizar]['cantidad']}.")
            while True:
                try:
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{nombre_a_actualizar}': "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")
            inventario[nombre_a_actualizar]['cantidad'] = nueva_cantidad
            print(f"Stock de '{nombre_a_actualizar}' actualizado a {nueva_cantidad}.")

    elif opcion == '3':
        print("\n--- Quitar Productos del Inventario ---")
        nombre_a_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
        if nombre_a_eliminar not in inventario:
            print(f"Error: El producto '{nombre_a_eliminar}' no se encuentra en el inventario.")
        else:
            confirmacion = input(f"¿Está seguro de que desea eliminar '{nombre_a_eliminar}' del inventario? (s/n): ").lower()
            if confirmacion == 's':
                del inventario[nombre_a_eliminar]
                print(f"Producto '{nombre_a_eliminar}' eliminado exitosamente.")
            else:
                print("Eliminación cancelada.")

    elif opcion == '4':
        print("\n--- Lista Actual de Productos ---")
        if not inventario:
            print("El inventario está vacío.")
        else:
            print(f"{'Producto':<15}{'Cantidad':<10}{'Precio':<10}")
            print("-" * 35)
            for nombre, detalles in inventario.items():
                print(f"{nombre:<15}{detalles['cantidad']:<10}{detalles['precio']:<10.2f}")

    elif opcion == '5':
        print("\n--- Buscar en el Inventario ---")
        termino_busqueda = input("Ingrese el nombre o parte del nombre del producto a buscar: ").strip().lower()
        productos_encontrados = []
        for nombre, detalles in inventario.items():
            if termino_busqueda in nombre.lower():
                productos_encontrados.append((nombre, detalles))

        if productos_encontrados:
            print("\n--- Resultados Encontrados ---")
            for nombre, detalles in productos_encontrados:
                print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']:.2f}")
        else:
            print(f"No se encontraron productos que coincidan con '{termino_busqueda}'.")

    elif opcion == '6':
        print("\n--- Estado General del Inventario ---")
        valor_total_inventario = 0
        print(f"{'Producto':<15}{'Cantidad':<10}{'Precio':<10}{'Total':<10}")
        print("-" * 50)
        for nombre, detalles in inventario.items():
            total = detalles['cantidad'] * detalles['precio']
            valor_total_inventario += total
            print(f"{nombre:<15}{detalles['cantidad']:<10}{detalles['precio']:<10.2f}{total:<10.2f}")
        print("-" * 50)
        print(f"Valor Total del Inventario: ${valor_total_inventario:.2f}")

        umbral_bajo_stock = 5
        productos_bajo_stock = [nombre for nombre, detalles in inventario.items() if detalles['cantidad'] < umbral_bajo_stock]

        if productos_bajo_stock:
            print(f"\nProductos con bajo stock (cantidad < {umbral_bajo_stock}):")
            for p in productos_bajo_stock:
                print(f"- {p} (Cantidad: {inventario[p]['cantidad']})")
        else:
            print("\nNo hay productos con bajo stock.")

        agotados = [nombre for nombre, detalles in inventario.items() if detalles['cantidad'] == 0]
        if agotados:
            print("\n¡Advertencia! Hay productos agotados:")
            for p in agotados:
                print(f"- {p}")
        else:
            print("\nNo hay productos agotados en el inventario.")

    elif opcion == '7':
        print("Programa finalizado. ¡Gracias por usar el sistema!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")



