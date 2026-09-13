class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            precio=float(datos["precio"]),
            stock=int(datos["stock"])
        )