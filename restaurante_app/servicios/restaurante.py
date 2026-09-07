from typing import List, Dict, Optional
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class Restaurante:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        
        # Colecciones principales (Listas)
        self.productos: List[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: List[Usuario] = self.archivo_servicio.cargar_usuarios()
        self.ventas: List[Venta] = self.archivo_servicio.cargar_ventas()
        
        # Índices auxiliares para optimización en memoria (Diccionarios)
        self._productos_index: Dict[str, Producto] = {}
        self._usuarios_index: Dict[str, Usuario] = {}
        self._ventas_por_usuario_index: Dict[str, List[Venta]] = {}
        
        # Reconstrucción inicial de índices
        self._reconstruir_indices()

    def _reconstruir_indices(self):
        """Pobla los diccionarios auxiliares a partir de las listas cargadas desde los JSON."""
        self._productos_index = {p.codigo: p for p in self.productos}
        self._usuarios_index = {u.identificacion: u for u in self.usuarios}
        
        self._ventas_por_usuario_index = {}
        for venta in self.ventas:
            if venta.usuario_id not in self._ventas_por_usuario_index:
                self._ventas_por_usuario_index[venta.usuario_id] = []
            self._ventas_por_usuario_index[venta.usuario_id].append(venta)

    # Búsquedas optimizadas O(1)
    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        return self._productos_index.get(codigo)

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        return self._usuarios_index.get(identificacion)

    def registrar_usuario(self, usuario: Usuario):
        if usuario.identificacion in self._usuarios_index:
            raise ValueError(f"El usuario con ID '{usuario.identificacion}' ya está registrado.")
        
        # Sincronización: lista + índice
        self.usuarios.append(usuario)
        self._usuarios_index[usuario.identificacion] = usuario
        self.archivo_servicio.guardar_usuarios(self.usuarios)

    def registrar_producto(self, producto: Producto):
        if producto.codigo in self._productos_index:
            raise ValueError(f"El producto con código '{producto.codigo}' ya existe.")
        
        # Sincronización: lista + índice
        self.productos.append(producto)
        self._productos_index[producto.codigo] = producto
        self.archivo_servicio.guardar_productos(self.productos)

    def realizar_venta(self, usuario_id: str, producto_codigo: str, cantidad: int) -> Venta:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
            
        usuario = self.buscar_usuario(usuario_id)
        if not usuario:
            raise ValueError(f"No existe un usuario registrado con ID '{usuario_id}'.")
            
        producto = self.buscar_producto(producto_codigo)
        if not producto:
            raise ValueError(f"No existe un producto con el código '{producto_codigo}'.")
            
        if producto.stock < cantidad:
            raise ValueError(f"Stock insuficiente. Stock actual: {producto.stock}")

        # Actualización de stock
        producto.stock -= cantidad

        nueva_venta = Venta(usuario_id, producto_codigo, cantidad)
        
        # Sincronización de lista e índice de ventas
        self.ventas.append(nueva_venta)
        if usuario_id not in self._ventas_por_usuario_index:
            self._ventas_por_usuario_index[usuario_id] = []
        self._ventas_por_usuario_index[usuario_id].append(nueva_venta)

        # Persistencia en JSON
        self.archivo_servicio.guardar_productos(self.productos)
        self.archivo_servicio.guardar_ventas(self.ventas)
        
        return nueva_venta

    def obtener_ventas_por_usuario(self, usuario_id: str) -> List[Venta]:
        """Consulta optimizada O(1) usando el índice agrupado por usuario."""
        return self._ventas_por_usuario_index.get(usuario_id, [])