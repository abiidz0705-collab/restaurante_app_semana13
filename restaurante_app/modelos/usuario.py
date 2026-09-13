class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str, clave: str = "1234"):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.clave = clave

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"],
            clave=datos.get("clave", "1234")
        )