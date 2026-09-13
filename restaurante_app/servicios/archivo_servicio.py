import json
import os

class ArchivoServicio:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR_DATOS = os.path.join(BASE_DIR, "datos")
    
    RUTA_PRODUCTOS = os.path.join(DIR_DATOS, "productos.json")
    RUTA_USUARIOS = os.path.join(DIR_DATOS, "usuarios.json")

    def __init__(self):
        if not os.path.exists(self.DIR_DATOS):
            os.makedirs(self.DIR_DATOS, exist_ok=True)

    def cargar_productos(self) -> list:
        if not os.path.exists(self.RUTA_PRODUCTOS):
            return []
        try:
            with open(self.RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def cargar_usuarios(self) -> list:
        if not os.path.exists(self.RUTA_USUARIOS):
            return []
        try:
            with open(self.RUTA_USUARIOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []