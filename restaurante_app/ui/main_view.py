import tkinter as tk
from tkinter import ttk, messagebox

class MainView(ttk.Frame):
    def __init__(self, parent, restaurante_servicio, on_logout):
        super().__init__(parent)
        self.servicio = restaurante_servicio
        self.on_logout = on_logout

        self._crear_interfaz()

    def _crear_interfaz(self):
        # Header / Barra superior
        header_frame = ttk.Frame(self, padding=10)
        header_frame.pack(fill="x", side="top")

        lbl_titulo = ttk.Label(
            header_frame, 
            text="Sistema de Gestión - Restaurante App", 
            font=("Arial", 14, "bold")
        )
        lbl_titulo.pack(side="left")

        btn_logout = ttk.Button(
            header_frame, 
            text="Cerrar Sesión", 
            command=self.on_logout
        )
        btn_logout.pack(side="right")

        # Contenedor principal de pestañas
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 1: Productos (CRUD Completo)
        tab_productos = ttk.Frame(notebook)
        notebook.add(tab_productos, text="Productos")
        self._construir_tab_productos(tab_productos)

        # Pestaña 2: Usuarios (Consulta)
        tab_usuarios = ttk.Frame(notebook)
        notebook.add(tab_usuarios, text="Usuarios Registrados")
        self._construir_tab_usuarios(tab_usuarios)

        # Pestaña 3: Ventas (Pendiente)
        tab_ventas = ttk.Frame(notebook)
        notebook.add(tab_ventas, text="Ventas (Pendiente)")
        self._construir_tab_ventas(tab_ventas)

    def _construir_tab_productos(self, parent):
        # Panel Izquierdo: Formulario en LabelFrame
        frame_form = ttk.LabelFrame(parent, text=" Formulario de Producto ", padding=10)
        frame_form.pack(side="left", fill="y", padx=10, pady=10)

        ttk.Label(frame_form, text="ID / Código:").grid(row=0, column=0, sticky="w", pady=5)
        self.txt_id = ttk.Entry(frame_form, width=20)
        self.txt_id.grid(row=0, column=1, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nombre = ttk.Entry(frame_form, width=20)
        self.txt_nombre.grid(row=1, column=1, pady=5)

        ttk.Label(frame_form, text="Precio ($):").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_precio = ttk.Entry(frame_form, width=20)
        self.txt_precio.grid(row=2, column=1, pady=5)

        ttk.Label(frame_form, text="Categoría:").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_categoria = ttk.Entry(frame_form, width=20)
        self.txt_categoria.grid(row=3, column=1, pady=5)

        # Contenedor de Botones (usando padding en lugar de pady)
        frame_botones = ttk.Frame(frame_form, padding=(0, 10))
        frame_botones.grid(row=4, column=0, columnspan=2)

        ttk.Button(frame_botones, text="Registrar", command=self._registrar_producto).grid(row=0, column=0, padx=2, pady=2)
        ttk.Button(frame_botones, text="Consultar", command=self._consultar_producto).grid(row=0, column=1, padx=2, pady=2)
        ttk.Button(frame_botones, text="Actualizar", command=self._actualizar_producto).grid(row=1, column=0, padx=2, pady=2)
        ttk.Button(frame_botones, text="Eliminar", command=self._eliminar_producto).grid(row=1, column=1, padx=2, pady=2)
        ttk.Button(frame_botones, text="Limpiar", command=self._limpiar_formulario).grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

        # Panel Derecho: Tabla de visualización Treeview
        frame_tabla = ttk.LabelFrame(parent, text=" Lista de Productos ", padding=10)
        frame_tabla.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        columnas = ("id", "nombre", "precio", "categoria")
        self.tabla_prod = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        self.tabla_prod.heading("id", text="ID")
        self.tabla_prod.heading("nombre", text="Nombre")
        self.tabla_prod.heading("precio", text="Precio ($)")
        self.tabla_prod.heading("categoria", text="Categoría")

        self.tabla_prod.column("id", width=60, anchor="center")
        self.tabla_prod.column("nombre", width=140)
        self.tabla_prod.column("precio", width=80, anchor="e")
        self.tabla_prod.column("categoria", width=100)

        scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla_prod.yview)
        self.tabla_prod.configure(yscrollcommand=scroll.set)

        self.tabla_prod.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self._cargar_tabla_productos()

    def _cargar_tabla_productos(self):
        for item in self.tabla_prod.get_children():
            self.tabla_prod.delete(item)
        for p in self.servicio.obtener_productos():
            p_id = getattr(p, "id_prod", getattr(p, "id", ""))
            p_cat = getattr(p, "categoria", "General")
            self.tabla_prod.insert("", "end", values=(p_id, p.nombre, f"{p.precio:.2f}", p_cat))

    def _limpiar_formulario(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_categoria.delete(0, tk.END)

    def _registrar_producto(self):
        exito, msg = self.servicio.registrar_producto(
            self.txt_id.get().strip(),
            self.txt_nombre.get().strip(),
            self.txt_precio.get().strip(),
            self.txt_categoria.get().strip()
        )
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._cargar_tabla_productos()
            self._limpiar_formulario()
        else:
            messagebox.showwarning("Error", msg)

    def _consultar_producto(self):
        id_prod = self.txt_id.get().strip()
        if not id_prod:
            messagebox.showwarning("Atención", "Ingrese un ID de producto para consultar.")
            return
        prod = self.servicio.buscar_producto_por_id(id_prod)
        if prod:
            self._limpiar_formulario()
            p_id = getattr(prod, "id_prod", getattr(prod, "id", ""))
            p_cat = getattr(prod, "categoria", "General")
            self.txt_id.insert(0, p_id)
            self.txt_nombre.insert(0, prod.nombre)
            self.txt_precio.insert(0, str(prod.precio))
            self.txt_categoria.insert(0, p_cat)
            messagebox.showinfo("Encontrado", f"Producto '{prod.nombre}' cargado en el formulario.")
        else:
            messagebox.showerror("Error", "No se encontró ningún producto con ese ID.")

    def _actualizar_producto(self):
        exito, msg = self.servicio.actualizar_producto(
            self.txt_id.get().strip(),
            self.txt_nombre.get().strip(),
            self.txt_precio.get().strip(),
            self.txt_categoria.get().strip()
        )
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._cargar_tabla_productos()
            self._limpiar_formulario()
        else:
            messagebox.showwarning("Error", msg)

    def _eliminar_producto(self):
        id_prod = self.txt_id.get().strip()
        if not id_prod:
            messagebox.showwarning("Atención", "Ingrese el ID del producto que desea eliminar.")
            return
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto con ID {id_prod}?"):
            exito, msg = self.servicio.eliminar_producto(id_prod)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._cargar_tabla_productos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", msg)

    def _construir_tab_usuarios(self, parent):
        frame_tabla = ttk.LabelFrame(parent, text=" Usuarios Registrados ", padding=10)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        columnas = ("id", "nombre", "correo")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        tabla.heading("id", text="Identificación")
        tabla.heading("nombre", text="Nombre Completo")
        tabla.heading("correo", text="Correo Electrónico")

        for u in self.servicio.obtener_usuarios():
            tabla.insert("", "end", values=(u.identificacion, u.nombre, u.correo))

        tabla.pack(fill="both", expand=True)

    def _construir_tab_ventas(self, parent):
        frame_info = ttk.Frame(parent, padding=20)
        frame_info.pack(fill="both", expand=True)

        lbl = ttk.Label(
            frame_info, 
            text="Módulo de Ventas en desarrollo.\nEsta funcionalidad se integrará en las siguientes semanas.", 
            font=("Arial", 11, "italic"),
            justify="center"
        )
        lbl.pack(expand=True)