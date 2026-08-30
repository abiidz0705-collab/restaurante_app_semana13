import sys
from typing import Dict, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
servicio_restaurante = Restaurante()
servicio_archivo = ArchivoServicio()

def sincronizar_todo() -> None:
    servicio_archivo.guardar_productos(servicio_restaurante.obtener_productos())
    servicio_archivo.guardar_usuarios(servicio_restaurante.obtener_usuarios())
    servicio_archivo.guardar_ventas(servicio_restaurante.obtener_ventas())

def opcion_registrar_usuario() -> None:
    print("\n--- REGISTRAR USUARIO ---")
    identificacion = input("ID/Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    try:
        usuario = Usuario(identificacion, nombre, correo)
        if servicio_restaurante.registrar_usuario(usuario):
            sincronizar_todo()
            print("¡Usuario registrado con éxito!")
        else:
            print("Error: Ya existe un usuario con esa identificación.")
    except ValueError as err:
        print(f"Error: {err}")

def opcion_registrar_producto() -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        producto = Producto(codigo, nombre, categoria, precio, stock)
        if servicio_restaurante.registrar_producto(producto):
            sincronizar_todo()
            print("¡Producto registrado exitosamente!")
        else:
            print("Error: Código duplicado.")
    except ValueError as err:
        print(f"Error: {err}")

def opcion_vender_producto() -> None:
    print("\n--- REALIZAR VENTA ---")
    id_usuario = input("ID del Usuario: ").strip()
    cod_producto = input("Código del Producto: ").strip()
    try:
        cantidad = int(input("Cantidad a comprar: "))
        if servicio_restaurante.vender_producto(cod_producto, id_usuario, cantidad):
            sincronizar_todo()
            print("¡Venta realizada con éxito y stock actualizado!")
        else:
            print("Error: Usuario/Producto no encontrado o stock insuficiente.")
    except ValueError as err:
        print(f"Error: {err}")

def opcion_consultar_ventas_usuario() -> None:
    print("\n--- CONSULTAR VENTAS POR USUARIO ---")
    id_usuario = input("ID del Usuario: ").strip()
    ventas = servicio_restaurante.obtener_ventas_por_usuario(id_usuario)
    if not ventas:
        print("No se encontraron ventas para este usuario.")
    else:
        for v in ventas:
            prod = servicio_restaurante.buscar_producto_por_codigo(v.producto_codigo)
            nombre_prod = prod.nombre if prod else "Producto desconocido"
            print(f"- Producto: {nombre_prod} (Cód: {v.producto_codigo}) | Cantidad: {v.cantidad}")

def opcion_listar_productos() -> None:
    print("\n--- CATALOGO DE PRODUCTOS ---")
    for p in servicio_restaurante.obtener_productos():
        print(p.mostrar_informacion())

def opcion_salir() -> None:
    print("\nSaliendo del sistema...")
    sys.exit()

def ejecutar() -> None:
    # Cargar datos guardados
    servicio_restaurante.cargar_datos(
        servicio_archivo.cargar_productos(),
        servicio_archivo.cargar_usuarios(),
        servicio_archivo.cargar_ventas()
    )

    menu: Dict[str, Callable[[], None]] = {
        "1": opcion_registrar_usuario,
        "2": opcion_registrar_producto,
        "3": opcion_vender_producto,
        "4": opcion_consultar_ventas_usuario,
        "5": opcion_listar_productos,
        "6": opcion_salir
    }

    while True:
        print("\n====================================")
        print("     SISTEMA RESTAURANTE - SEMANA 11")
        print("====================================")
        print("1. Registrar usuario")
        print("2. Registrar producto")
        print("3. Realizar venta")
        print("4. Consultar ventas por usuario")
        print("5. Listar productos (ver stock)")
        print("6. Salir")
        print("====================================")
        opcion = input("Elija una opción (1-6): ").strip()
        accion = menu.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar()