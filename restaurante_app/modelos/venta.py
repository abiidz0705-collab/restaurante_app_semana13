from datetime import datetime

class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int, fecha: str = None):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=int(datos["cantidad"]),
            fecha=datos.get("fecha")
        )