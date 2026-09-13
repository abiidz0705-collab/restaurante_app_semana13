import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, servicio, on_login_success):
        super().__init__(parent)
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.pack(fill="both", expand=True)
        self._crear_componentes()

    def _crear_componentes(self):
        frame_box = tk.LabelFrame(self, text=" Acceso al Sistema - Restaurante App ", padx=20, pady=20)
        frame_box.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_box, text="Identificación / ID:").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_usuario = tk.Entry(frame_box, width=25)
        self.ent_usuario.grid(row=0, column=1, pady=5)

        tk.Label(frame_box, text="Contraseña:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_clave = tk.Entry(frame_box, width=25, show="*")
        self.ent_clave.grid(row=1, column=1, pady=5)

        btn_ingresar = tk.Button(frame_box, text="Ingresar", command=self._ejecutar_login, bg="#2196F3", fg="white", width=15)
        btn_ingresar.grid(row=2, column=0, columnspan=2, pady=15)

    def _ejecutar_login(self):
        usuario = self.ent_usuario.get().strip()
        clave = self.ent_clave.get().strip()

        if not usuario or not clave:
            messagebox.showwarning("Atención", "Por favor complete todos los campos.")
            return

        if self.servicio.validar_acceso(usuario, clave):
            self.ent_usuario.delete(0, tk.END)
            self.ent_clave.delete(0, tk.END)
            self.on_login_success()
        else:
            messagebox.showerror("Error de Autenticación", "Identificación o contraseña incorrectos.")