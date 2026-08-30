import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    
    # Construye la ruta absoluta a la carpeta "datos" dentro del paquete restaurante_app
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR_DATOS = os.path.join(BASE_DIR, "datos")
    
    RUTA_PRODUCTOS = os.path.join(DIR_DATOS, "productos.json")
    RUTA_USUARIOS = os.path.join(DIR_DATOS, "usuarios.json")
    RUTA_VENTAS = os.path.join(DIR_DATOS, "ventas.json")

    def __init__(self) -> None:
        if not os.path.exists(self.DIR_DATOS):
            os.makedirs(self.DIR_DATOS)

    # --- PRODUCTOS ---
    def guardar_productos(self, productos: List[Producto]) -> None:
        with open(self.RUTA_PRODUCTOS, "w", encoding="utf-8") as f:
            json.dump([p.a_diccionario() for p in productos], f, indent=4, ensure_ascii=False)

    def cargar_productos(self) -> List[Producto]:
        if not os.path.exists(self.RUTA_PRODUCTOS):
            return []
        try:
            with open(self.RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Producto.desde_diccionario(item) for item in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
            return []

    # --- USUARIOS ---
    def guardar_usuarios(self, usuarios: List[Usuario]) -> None:
        with open(self.RUTA_USUARIOS, "w", encoding="utf-8") as f:
            json.dump([u.a_diccionario() for u in usuarios], f, indent=4, ensure_ascii=False)

    def cargar_usuarios(self) -> List[Usuario]:
        if not os.path.exists(self.RUTA_USUARIOS):
            return []
        try:
            with open(self.RUTA_USUARIOS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario.desde_diccionario(item) for item in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
            return []

    # --- VENTAS ---
    def guardar_ventas(self, ventas: List[Venta]) -> None:
        with open(self.RUTA_VENTAS, "w", encoding="utf-8") as f:
            json.dump([v.a_diccionario() for v in ventas], f, indent=4, ensure_ascii=False)

    def cargar_ventas(self) -> List[Venta]:
        if not os.path.exists(self.RUTA_VENTAS):
            return []
        try:
            with open(self.RUTA_VENTAS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Venta.desde_diccionario(item) for item in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
            return []