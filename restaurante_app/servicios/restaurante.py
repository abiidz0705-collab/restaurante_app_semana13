from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class Restaurante:
    """Administra la lógica de negocio del sistema."""

    def __init__(self) -> None:
        self.lista_productos: List[Producto] = []
        self.lista_usuarios: List[Usuario] = []
        self.lista_ventas: List[Venta] = []

    # Carga inicial
    def cargar_datos(self, productos: List[Producto], usuarios: List[Usuario], ventas: List[Venta]) -> None:
        self.lista_productos = productos
        self.lista_usuarios = usuarios
        self.lista_ventas = ventas

    # --- USUARIOS ---
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario_por_id(usuario.identificacion) is None:
            self.lista_usuarios.append(usuario)
            return True
        return False

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        for u in self.lista_usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def obtener_usuarios(self) -> List[Usuario]:
        return self.lista_usuarios

    # --- PRODUCTOS ---
    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto_por_codigo(producto.codigo) is None:
            self.lista_productos.append(producto)
            return True
        return False

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self.lista_productos:
            if p.codigo == codigo:
                return p
        return None

    def obtener_productos(self) -> List[Producto]:
        return self.lista_productos

    # --- VENTAS ---
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario_por_id(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        # Descontar stock y registrar venta
        producto.vender(cantidad)
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self.lista_ventas.append(venta)
        return True

    def obtener_ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        ventas_usuario: List[Venta] = []
        for venta in self.lista_ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    def obtener_ventas(self) -> List[Venta]:
        return self.lista_ventas