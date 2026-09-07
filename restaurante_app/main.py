def main():
    restaurante = Restaurante()

    while True:
        print("\n==========================================")
        print("       SISTEMA RESTAURANTE - SEMANA 12    ")
        print("==========================================")
        print("1. Registrar usuario")
        print("2. Registrar producto")
        print("3. Buscar producto por código")
        print("4. Buscar usuario por identificación")
        print("5. Realizar venta")
        print("6. Consultar ventas por usuario")
        print("7. Listar todos los productos")
        print("8. Ejecutar prueba de rendimiento (Métricas)")
        print("9. Salir")
        print("==========================================")

        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            registrar_usuario_menu(restaurante)
        elif opcion == "2":
            registrar_producto_menu(restaurante)
        elif opcion == "3":
            buscar_producto_menu(restaurante)
        elif opcion == "4":
            buscar_usuario_menu(restaurante)
        elif opcion == "5":
            realizar_venta_menu(restaurante)
        elif opcion == "6":
            consultar_ventas_menu(restaurante)
        elif opcion == "7":
            listar_productos_menu(restaurante)
        elif opcion == "8":
            ejecutar_prueba_rendimiento(restaurante)
        elif opcion == "9":
            print(">> Saliendo del sistema...")
            break
        else:
            print(">> Opción no válida. Intente de nuevo.")