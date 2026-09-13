import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, parent, servicio, on_logout):
        super().__init__(parent)
        self.servicio = servicio
        self.on_logout = on_logout

        self.pack(fill="both", expand=True)
        self._crear_interfaz()

    def _crear_interfaz(self):
        # Encabezado
        frame_top = tk.Frame(self, bg="#333", height=50)
        frame_top.pack(fill="x", side="top")

        lbl_titulo = tk.Label(frame_top, text="RESTAURANTE APP - PANEL PRINCIPAL", fg="white", bg="#333", font=("Arial", 12, "bold"))
        lbl_titulo.pack(side="left", padx=15, pady=10)

        btn_cerrar = tk.Button(frame_top, text="Cerrar Sesión", command=self._cerrar_sesion, bg="#f44336", fg="white")
        btn_cerrar.pack(side="right", padx=15, pady=10)

        # Panel de Pestañas (Notebook)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text=" Catálogo de Productos ")
        self._construir_pestana_productos()

        # Pestaña Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text=" Usuarios Registrados ")
        self._construir_pestana_usuarios()

        # Pestaña Ventas (Pendiente)
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text=" Ventas ")
        self._construir_pestana_ventas()

    def _construir_pestana_productos(self):
        tabla = ttk.Treeview(self.tab_productos, columns=("codigo", "nombre", "precio", "stock"), show="headings")
        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre del Producto")
        tabla.heading("precio", text="Precio ($)")
        tabla.heading("stock", text="Stock")

        tabla.column("codigo", width=100, anchor="center")
        tabla.column("nombre", width=250)
        tabla.column("precio", width=100, anchor="center")
        tabla.column("stock", width=100, anchor="center")

        tabla.pack(fill="both", expand=True, padx=5, pady=5)

        for p in self.servicio.obtener_productos():
            tabla.insert("", "end", values=(p.codigo, p.nombre, f"{p.precio:.2f}", p.stock))

    def _construir_pestana_usuarios(self):
        tabla = ttk.Treeview(self.tab_usuarios, columns=("id", "nombre", "correo"), show="headings")
        tabla.heading("id", text="Identificación")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("correo", text="Correo Electrónico")

        tabla.column("id", width=120, anchor="center")
        tabla.column("nombre", width=200)
        tabla.column("correo", width=250)

        tabla.pack(fill="both", expand=True, padx=5, pady=5)

        for u in self.servicio.obtener_usuarios():
            tabla.insert("", "end", values=(u.identificacion, u.nombre, u.correo))

    def _construir_pestana_ventas(self):
        lbl_info = tk.Label(self.tab_ventas, text="Módulo de Ventas en desarrollo (Evolución Semana 14).\nFuncionalidad pendiente.", font=("Arial", 11, "italic"), fg="gray")
        lbl_info.pack(expand=True)

    def _cerrar_sesion(self):
        self.servicio.cerrar_sesion()
        self.on_logout()