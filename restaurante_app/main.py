import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Tkinter GUI")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # Iniciar servicio central
        self.servicio = RestauranteServicio()

        self.vista_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.vista_actual:
            self.vista_actual.destroy()

        self.vista_actual = LoginView(self.root, self.servicio, on_login_success=self.mostrar_main)

    def mostrar_main(self):
        if self.vista_actual:
            self.vista_actual.destroy()

        self.vista_actual = MainView(self.root, self.servicio, on_logout=self.mostrar_login)

def main():
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()