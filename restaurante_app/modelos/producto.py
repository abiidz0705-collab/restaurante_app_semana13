class Producto:
    def __init__(self, id_prod, nombre, precio, categoria="General"):
        self.id_prod = id_prod
        self.id = id_prod  # Guardamos ambos para evitar cualquier desfase
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id_prod,
            "id_prod": self.id_prod,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }