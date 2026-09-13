from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.usuario_actual: Usuario | None = None
        
        self.cargar_datos()

    def cargar_datos(self):
        datos_prod = self.archivo_servicio.cargar_productos()
        self.productos = [Producto.desde_diccionario(p) for p in datos_prod]

        datos_usu = self.archivo_servicio.cargar_usuarios()
        self.usuarios = [Usuario.desde_diccionario(u) for u in datos_usu]

    def validar_acceso(self, identificacion: str, clave: str) -> bool:
        for u in self.usuarios:
            if u.identificacion == identificacion and u.clave == clave:
                self.usuario_actual = u
                return True
        return False

    def obtener_productos(self) -> list[Producto]:
        return self.productos

    def obtener_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def cerrar_sesion(self):
        self.usuario_actual = None