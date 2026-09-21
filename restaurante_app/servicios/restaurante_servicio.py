from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        self.productos = []
        self.usuarios = []
        self._cargar_datos()

    def _obtener_id_producto(self, p):
        # Busca el atributo de ID independientemente del nombre exacto en la clase Producto
        for attr in ["id", "id_prod", "_id", "codigo"]:
            if hasattr(p, attr):
                val = getattr(p, attr)
                if val is not None and str(val).strip() != "":
                    return str(val)
        return ""

    def _cargar_datos(self):
        datos_prod = self.archivo_servicio.cargar_productos()
        self.productos = []
        for p in datos_prod:
            id_val = str(p.get("id") or p.get("id_prod") or p.get("codigo") or "")
            nom_val = str(p.get("nombre") or "")
            precio_val = float(p.get("precio", 0))
            cat_val = str(p.get("categoria") or "General")

            prod_obj = Producto(id_val, nom_val, precio_val, cat_val)
            # Asegura que el atributo id o id_prod quede explícitamente asignado
            if hasattr(prod_obj, "id_prod"):
                prod_obj.id_prod = id_val
            if hasattr(prod_obj, "id"):
                prod_obj.id = id_val

            self.productos.append(prod_obj)

        datos_usu = self.archivo_servicio.cargar_usuarios()
        self.usuarios = []
        for u in datos_usu:
            self.usuarios.append(Usuario(
                u.get("identificacion"),
                u.get("nombre"),
                u.get("correo"),
                u.get("clave")
            ))

    def _guardar_productos(self):
        lista_dict = []
        for p in self.productos:
            if hasattr(p, "to_dict"):
                lista_dict.append(p.to_dict())
            else:
                p_id = self._obtener_id_producto(p)
                p_cat = getattr(p, "categoria", "General")
                lista_dict.append({
                    "id": p_id,
                    "nombre": p.nombre,
                    "precio": p.precio,
                    "categoria": p_cat
                })
        return self.archivo_servicio.guardar_productos(lista_dict)

    def validar_acceso(self, identificacion, clave):
        for u in self.usuarios:
            if u.identificacion == identificacion and u.clave == clave:
                return True
        return False

    def obtener_productos(self):
        return self.productos

    def obtener_usuarios(self):
        return self.usuarios

    def buscar_producto_por_id(self, id_prod):
        id_prod_str = str(id_prod).strip()
        for p in self.productos:
            p_id = self._obtener_id_producto(p)
            if p_id == id_prod_str:
                return p
        return None

    def registrar_producto(self, id_prod, nombre, precio, categoria):
        id_prod_clean = str(id_prod).strip()
        nombre_clean = str(nombre).strip()
        
        if not id_prod_clean or not nombre_clean:
            return False, "El ID y Nombre son obligatorios."
        if self.buscar_producto_por_id(id_prod_clean):
            return False, "Ya existe un producto con este ID."
        try:
            precio_val = float(precio)
        except ValueError:
            return False, "El precio debe ser un número válido."

        cat_clean = str(categoria).strip() if categoria else "General"
        nuevo = Producto(id_prod_clean, nombre_clean, precio_val, cat_clean)
        
        if hasattr(nuevo, "id_prod"):
            nuevo.id_prod = id_prod_clean
        if hasattr(nuevo, "id"):
            nuevo.id = id_prod_clean

        self.productos.append(nuevo)
        self._guardar_productos()
        return True, "Producto registrado con éxito."

    def actualizar_producto(self, id_prod, nombre, precio, categoria):
        id_prod_clean = str(id_prod).strip()
        prod = self.buscar_producto_por_id(id_prod_clean)
        if not prod:
            return False, "El producto no existe."
        try:
            precio_val = float(precio)
        except ValueError:
            return False, "El precio debe ser un número válido."

        prod.nombre = str(nombre).strip()
        prod.precio = precio_val
        if hasattr(prod, "categoria"):
            prod.categoria = str(categoria).strip() if categoria else "General"
            
        self._guardar_productos()
        return True, "Producto actualizado con éxito."

    def eliminar_producto(self, id_prod):
        id_prod_clean = str(id_prod).strip()
        prod = self.buscar_producto_por_id(id_prod_clean)
        if not prod:
            return False, "El producto no existe."
        self.productos.remove(prod)
        self._guardar_productos()
        return True, "Producto eliminado correctamente."