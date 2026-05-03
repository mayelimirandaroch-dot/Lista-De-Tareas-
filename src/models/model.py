import json
from collections import deque  # --> cola FIFO: agrega por derecha, saca por izquierda


# ─────────────────────────────────────────────
#  MODELO - GESTOR DE TAREAS
# ─────────────────────────────────────────────
class GestorTareas:
    def __init__(self, nombre_sistema: str):
        """
        Inicializa el gestor de tareas.

        Args:
            nombre_sistema (str): Nombre del sistema. Ej: 'Impresora Oficina A'.
        """
        self.nombre_sistema  = nombre_sistema
        self.cola_tareas     = deque()   # cola FIFO de tareas pendientes
        self.historial_pila  = []        # pila de tareas procesadas
        self.contador        = 0         # contador global de tareas

    # ─────────────────────────────────────────
    #  AGREGAR TAREA
    # ─────────────────────────────────────────
    def agregar_tarea(self, nombre: str, tipo: str) -> str:
        """
        Agrega una nueva tarea al final de la cola (FIFO).

        Args:
            nombre (str): Nombre o descripción de la tarea.
            tipo (str): Tipo de tarea. Ej: 'impresión', 'escaneo', 'copia'.

        Returns:
            str: ID único asignado a la tarea. Ej: 'T-001'.
        """
        self.contador += 1
        tarea_id = f"T-{self.contador:03d}"
        tarea = {
            "id"       : tarea_id,
            "nombre"   : nombre,
            "tipo"     : tipo,
            "estado"   : "pendiente"
        }
        self.cola_tareas.append(tarea)  # agrega al final de la cola (FIFO)
        return tarea_id

    # ─────────────────────────────────────────
    #  PROCESAR SIGUIENTE TAREA
    # ─────────────────────────────────────────
    def procesar_siguiente(self) -> dict | None:
        """
        Procesa la siguiente tarea del frente de la cola (FIFO).

        Returns:
            dict: Datos de la tarea procesada, o None si la cola está vacía.
        """
        if not self.cola_tareas:
            return None
        tarea = self.cola_tareas.popleft()  # saca del frente (FIFO)
        tarea["estado"] = "procesada"
        self.historial_pila.append(tarea)   # apila en historial
        return tarea

    # ─────────────────────────────────────────
    #  PROCESAR POR LOTES
    # ─────────────────────────────────────────
    def procesar_lote(self, cantidad: int) -> list:
        """
        Procesa un lote de tareas del frente de la cola.

        Args:
            cantidad (int): Número de tareas a procesar en este lote.

        Returns:
            list: Lista de tareas procesadas en este lote.
        """
        procesadas = []
        for _ in range(cantidad):
            tarea = self.procesar_siguiente()
            if tarea is None:
                break  # cola vacía antes de completar el lote
            procesadas.append(tarea)
        return procesadas

    # ─────────────────────────────────────────
    #  VER COLA
    # ─────────────────────────────────────────
    def ver_cola(self) -> list:
        """
        Retorna la lista de tareas pendientes en orden FIFO.

        Returns:
            list: Lista de dicts con las tareas pendientes.
        """
        return list(self.cola_tareas)

    # ─────────────────────────────────────────
    #  HISTORIAL
    # ─────────────────────────────────────────
    def historial(self, n: int = 10) -> list:
        """
        Retorna las últimas n tareas procesadas.

        Args:
            n (int): Cantidad de tareas a retornar. Por defecto 10.

        Returns:
            list: Últimas n tareas procesadas, más reciente primero.
        """
        return self.historial_pila[-n:][::-1]  # últimas n, invertidas (más reciente primero)

    # ─────────────────────────────────────────
    #  CANCELAR TAREA
    # ─────────────────────────────────────────
    def cancelar_tarea(self, tarea_id: str) -> bool:
        """
        Cancela y elimina una tarea pendiente de la cola por su ID.

        Args:
            tarea_id (str): ID de la tarea a cancelar. Ej: 'T-003'.

        Returns:
            bool: True si fue cancelada, False si no se encontró.
        """
        for tarea in self.cola_tareas:
            if tarea["id"] == tarea_id:
                self.cola_tareas.remove(tarea)
                return True
        return False

    # ─────────────────────────────────────────
    #  PERSISTENCIA JSON
    # ─────────────────────────────────────────
    def guardar_estado(self, archivo: str) -> None:
        """
        Persiste el estado completo del gestor en un archivo JSON.

        Args:
            archivo (str): Ruta del archivo JSON.
        """
        estado = {
            "nombre_sistema" : self.nombre_sistema,
            "cola_tareas"    : list(self.cola_tareas),   # deque → list para JSON
            "historial_pila" : self.historial_pila,
            "contador"       : self.contador
        }
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(estado, f, ensure_ascii=False, indent=2)

    @classmethod
    def cargar_estado(cls, archivo: str) -> "GestorTareas":
        """
        Restaura el estado del gestor desde un archivo JSON.

        Args:
            archivo (str): Ruta del archivo JSON.

        Returns:
            GestorTareas: Nueva instancia con el estado cargado.
        """
        with open(archivo, "r", encoding="utf-8") as f:
            estado = json.load(f)
        gestor = cls(estado["nombre_sistema"])
        gestor.cola_tareas    = deque(estado["cola_tareas"])  # list → deque
        gestor.historial_pila = estado["historial_pila"]
        gestor.contador       = estado["contador"]
        return gestor