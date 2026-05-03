# 🖨️ Gestor de Tareas - Impresora Virtual

**Autor:** Mayeli Miranda Rocha
**Registro:** 223043362
**Materia:** Estructuras de Datos I

Sistema de gestión de colas de impresión desarrollado en **Python** para la materia de Estructuras de Datos I. La aplicación simula el flujo de trabajo de una impresora utilizando estructuras de datos lineales para el manejo eficiente de tareas.

## 🚀 Características y Conceptos
* **Arquitectura MVC:** Separación clara entre la lógica de datos (`models`), la interfaz de usuario (`views`) y la lógica de control (`controllers`).
* **Estructuras de Datos:** 
  * **Colas (Queue):** Manejo de tareas pendientes siguiendo el principio **FIFO** (First In, First Out): lo primero que entra es lo primero que sale.
  * **Pilas (Stack):** Registro de historial de tareas completadas siguiendo el principio **LIFO** (Last In, First Out).
* **Persistencia:** Guardado automático del estado del sistema en archivos **JSON** dentro de la carpeta `src/datos/`.

## 📁 Estructura del Proyecto
* `src/main.py`: Punto de entrada principal de la aplicación.
* `src/models/`: Definición de la lógica de negocio y estructuras de datos.
* `src/views/`: Interfaz gráfica de usuario desarrollada en **Tkinter**.
* `src/controllers/`: Controladores que actúan como puente entre la vista y el modelo.

## 🛠️ Especificaciones Técnicas (Requirements)
### Backend & Frameworks
* **Framework UI:** Tkinter (Biblioteca estándar de Python).
* **Persistencia de Datos:** Implementación mediante archivos **JSON**, garantizando que las tareas no se pierdan al cerrar la aplicación.
* **Bibliotecas Clave:**
    * `collections.deque`: Utilizada para la implementación de la **Cola (Queue)**, optimizando el rendimiento de entrada y salida a $O(1)$.
    * `json`: Para el mapeo de objetos del modelo a archivos físicos.
    * `os`: Para la gestión de rutas y directorios de forma dinámica.

### Arquitectura de Software
El proyecto implementa el patrón **Model-View-Controller (MVC)**:
1. **Model (`src/models/model.py`):** Contiene la lógica de la Pila, la Cola y el manejo de datos.
2. **View (`src/views/view.py`):** Gestiona la renderización de la interfaz de usuario y captura de eventos.
3. **Controller (`src/controllers/controller.py`):** Orquestador de eventos y comunicación entre capas.

## 🚀 Instalación y Ejecución
1. Asegúrese de tener **Python 3.10+** instalado.
2. Navegue a la carpeta del código fuente:
   ```bash
   cd src