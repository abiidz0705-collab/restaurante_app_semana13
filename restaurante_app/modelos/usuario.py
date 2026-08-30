from typing import Dict, Any

class Usuario:
    """Clase que representa un usuario o cliente del restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion or not nombre:
            raise ValueError("La identificación y el nombre son obligatorios.")

        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def a_diccionario(self) -> Dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def desde_diccionario(cls, datos: Dict[str, Any]) -> "Usuario":
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"]
        )

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"