from typing import Dict, Any

class Producto:
    """Clase que representa un producto dentro del menú del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        if not codigo or not nombre:
            raise ValueError("El código y el nombre del producto no pueden estar vacíos.")
        if precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio
        self.stock: int = stock

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock del producto tras una venta válida."""
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock -= cantidad

    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte el objeto a un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, datos: Dict[str, Any]) -> "Producto":
        """Reconstruye un objeto Producto desde un diccionario."""
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=float(datos["precio"]),
            stock=int(datos.get("stock", 0))
        )

    def mostrar_informacion(self) -> str:
        return f"[{self.categoria.upper()}] Cód: {self.codigo} | {self.nombre} - Precio: ${self.precio:.2f} | Stock: {self.stock}"