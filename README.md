# 🖨️ Gestor de Tareas - Impresora Virtual

**Autor:** Mayeli Miranda Rocha[cite: 1]  
**Registro:** 223043362[cite: 1]  
**Materia:** Estructuras de Datos I[cite: 1]

Sistema de gestión de colas de impresión desarrollado en **Python** para la materia de Estructuras de Datos I[cite: 1]. La aplicación simula el flujo de trabajo de una impresora utilizando estructuras de datos lineales para el manejo eficiente de tareas[cite: 1].

## 🚀 Características y Conceptos
* **Arquitectura MVC:** Separación clara entre la lógica de datos (`models`), la interfaz de usuario (`views`) y la lógica de control (`controllers`)[cite: 1].
* **Estructuras de Datos:** 
  * **Colas (Queue):** Manejo de tareas pendientes siguiendo el principio **FIFO** (First In, First Out): lo primero que entra es lo primero que sale[cite: 1].
  * **Pilas (Stack):** Registro de historial de tareas completadas siguiendo el principio **LIFO** (Last In, First Out)[cite: 1].
* **Persistencia:** Guardado automático del estado del sistema en archivos **JSON** dentro de la carpeta `src/datos/`[cite: 1].

## 📁 Estructura del Proyecto
Basado en los archivos actuales del repositorio[cite: 1]:
* `src/main.py`: Punto de entrada principal de la aplicación[cite: 1].
* `src/models/`: Definición de la lógica de negocio y estructuras de datos[cite: 1].
* `src/views/`: Interfaz gráfica de usuario desarrollada en **Tkinter**[cite: 1].
* `src/controllers/`: Controladores que actúan como puente entre la vista y el modelo[cite: 1].

## 🛠️ Especificaciones Técnicas (Requirements)
### Backend & Frameworks
* **Framework UI:** Tkinter (Biblioteca estándar de Python)[cite: 1].
* **Persistencia de Datos:** Implementación mediante archivos **JSON**, garantizando que las tareas no se pierdan al cerrar la aplicación[cite: 1].
* **Bibliotecas Clave:**
    * `collections.deque`: Utilizada para la implementación de la **Cola (Queue)**, optimizando el rendimiento de entrada y salida a $O(1)$[cite: 1].
    * `json`: Para el mapeo de objetos del modelo a archivos físicos[cite: 1].
    * `os`: Para la gestión de rutas y directorios de forma dinámica[cite: 1].

### Arquitectura de Software
El proyecto implementa el patrón **Model-View-Controller (MVC)**[cite: 1]:
1. **Model (`src/models/model.py`):** Contiene la lógica de la Pila, la Cola y el manejo de datos[cite: 1].
2. **View (`src/views/view.py`):** Gestiona la renderización de la interfaz de usuario y captura de eventos[cite: 1].
3. **Controller (`src/controllers/controller.py`):** Orquestador de eventos y comunicación entre capas[cite: 1].

## 🚀 Instalación y Ejecución
1. Asegúrese de tener **Python 3.10+** instalado[cite: 1].
2. Navegue a la carpeta del código fuente:
   ```bash
   cd src