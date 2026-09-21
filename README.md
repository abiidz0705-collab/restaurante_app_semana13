# Restaurante App - Semana 14: Componentes y Contenedores

**Estudiante:** Abigail Deleg
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 14

##  Descripción del Proyecto
Este proyecto consiste en el desarrollo de una aplicación de escritorio para la gestión de un restaurante utilizando **Python** y **Tkinter**. La aplicación evoluciona la estructura previa integrando componentes visuales avanzadas, contenedores organizativos y un ciclo completo de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para productos, manteniendo una clara separación de responsabilidades e integración con persistencia JSON.

---

## Arquitectura y Estructura del Proyecto
El sistema sigue un patrón de diseño modular estricto:

restaurante_app/
│
├── datos/                  # Archivos JSON para persistencia de datos
│   ├── productos.json      # Almacenamiento de productos
│   └── usuarios.json       # Almacenamiento de usuarios del sistema
│
├── modelos/                # Definición de clases de entidad (POO)
│   ├── producto.py         # Modelo de la entidad Producto
│   └── usuario.py          # Modelo de la entidad Usuario
│
├── servicios/              # Lógica de negocio y persistencia
│   ├── archivo_servicio.py # Manejo de lectura/escritura JSON
│   └── restaurante_servicio.py # Gestión de lógica CRUD y validaciones
│
├── ui/                     # Interfaz Gráfica de Usuario (GUI con Tkinter)
│   ├── login_view.py       # Vista para autenticación de usuarios
│   └── main_view.py        # Vista principal con contenedores y formularios
│
├── main.py                 # Punto de entrada de la aplicación
└── README.md               # Documentación del sistema

---

## Componentes, Contenedores y Experiencia de Usuario (UX)
- **Contenedores:**
  - `ttk.Notebook`: Gestión de pestañas separadas (*Productos*, *Usuarios Registrados*, *Ventas*).
  - `ttk.LabelFrame`: Organización visual agrupada para el *Formulario de Producto* y la *Lista de Productos*.
  - `ttk.Frame`: Estructuración modular para cada sección de la aplicación.
- **Componentes:**
  - `ttk.Entry`: Cajas de texto para entrada de datos.
  - `ttk.Button`: Botones de acción (*Registrar*, *Consultar*, *Actualizar*, *Eliminar*, *Limpiar*, *Cerrar Sesión*).
  - `ttk.Treeview`: Tabla interactiva con barras de desplazamiento para listar datos estructurados.
  - `messagebox`: Avisos y confirmaciones de interacción con el usuario.

---

## Funcionalidades Implementadas
1. **Autenticación de Usuarios:** Control de acceso mediante credenciales almacenadas.
2. **Gestión de Productos (CRUD):**
   - **Registro:** Agregar nuevos productos con validación de ID único y precio numérico.
   - **Consulta:** Buscar productos por código para cargar sus datos en el formulario.
   - **Actualización:** Editar nombre, precio y categoría de productos existentes.
   - **Eliminación:** Remover productos con mensaje previo de confirmación.
3. **Persistencia Automática:** Todos los cambios se guardan e importan en tiempo real desde los archivos `.json`.

---

## Instrucciones de Ejecución

1. Clonar el repositorio o descargar el código fuente.
2. Abrir una terminal en la carpeta raíz del proyecto.
3. Ejecutar la aplicación con el siguiente comando:

```bash
python main.py