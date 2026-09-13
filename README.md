# Restaurante App - Semana 13 (Transición a GUI con Tkinter)

**Estudiante:** Abigail Deleg
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 13

Este proyecto marca la transición de `restaurante_app` desde una interfaz de consola hacia una Interfaz Gráfica de Usuario (GUI) utilizando **Tkinter**.

## Estrategia Arquitectónica

Se implementa una arquitectura por capas desacoplada:
* `datos/`: Archivos de almacenamiento JSON local.
* `modelos/`: Definición de clases representativas (`Producto` y `Usuario`).
* `servicios/`: Capa de lógica de negocio y persistencia (`RestauranteServicio` y `ArchivoServicio`).
* `ui/`: Vistas gráficas compuestas por `LoginView` (autenticación) y `MainView` (panel general de datos).
* `main.py`: Controlador principal que administra el ciclo de vida de la ventana única de Tkinter.

## Flujo de Navegación

1. **Pantalla de Acceso (LoginView):** Solicita credenciales. Valida la existencia mediante `RestauranteServicio`.
2. **Panel Principal (MainView):** Tras una autenticación válida, despliega pestañas para consultar los productos y usuarios cargados desde los JSON. Identifica el módulo de Ventas como pendiente.
3. **Cierre de Sesión:** Permite regresar a la pantalla de login dentro de la misma ventana de ejecución.

## Ejecución

```bash
python main.py