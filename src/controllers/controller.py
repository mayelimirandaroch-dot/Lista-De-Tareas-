from models.model import GestorTareas

class Controller:
    def __init__(self, model: GestorTareas, view, archivo_estado: str):
        """
        Controlador MVC — conecta el modelo con la vista.

        Args:
            model (GestorTareas): Instancia del gestor de tareas.
            view: Instancia de la vista tkinter.
            archivo_estado (str): Ruta del archivo JSON de persistencia.
        """
        self.model          = model
        self.view           = view
        self.archivo_estado = archivo_estado
        self.view.set_controller(self)
        self._refrescar()

    # ─────────────────────────────────────────
    #  AGREGAR TAREA
    # ─────────────────────────────────────────
    def agregar_tarea(self):
        """Valida el formulario y agrega una tarea al final de la cola."""
        nombre    = self.view.get_nombre()
        tipo      = self.view.get_tipo()

        if not nombre:
            self.view.mostrar_mensaje("⚠ Ingresa el nombre del documento.",
                                      color=self.view.COLOR_MSG_WARN)
            return

        tarea_id = self.model.agregar_tarea(nombre, tipo)
        self.view.limpiar_nombre()
        self.view.mostrar_mensaje(f"✓ Tarea {tarea_id} agregada a la cola.",
                                  color=self.view.COLOR_MSG_OK)
        self._refrescar()

    # ─────────────────────────────────────────
    #  PROCESAR SIGUIENTE
    # ─────────────────────────────────────────
    def procesar_siguiente(self):
        """Procesa la siguiente tarea del frente de la cola (FIFO)."""
        tarea = self.model.procesar_siguiente()
        if tarea:
            self.view.mostrar_mensaje(
                f"✓ Procesando: {tarea['id']} — {tarea['nombre']}",
                color=self.view.COLOR_MSG_INFO
            )
        else:
            self.view.mostrar_mensaje("⚠ No hay tareas en la cola.",
                                      color=self.view.COLOR_MSG_WARN)
        self._refrescar()

    # ─────────────────────────────────────────
    #  PROCESAR LOTE
    # ─────────────────────────────────────────
    def procesar_lote(self):
        """Procesa un lote de tareas según la cantidad ingresada."""
        try:
            cantidad = int(self.view.get_lote())
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            self.view.mostrar_mensaje("⚠ Ingresa una cantidad válida mayor a 0.",
                                      color=self.view.COLOR_MSG_WARN)
            return

        procesadas = self.model.procesar_lote(cantidad)

        if procesadas:
            self.view.mostrar_mensaje(
                f"✓ Lote procesado: {len(procesadas)} tarea(s) completadas.",
                color=self.view.COLOR_MSG_INFO
            )
        else:
            self.view.mostrar_mensaje("⚠ No hay tareas en la cola.",
                                      color=self.view.COLOR_MSG_WARN)
        self._refrescar()

    # ─────────────────────────────────────────
    #  CANCELAR TAREA
    # ─────────────────────────────────────────
    def cancelar_tarea(self):
        """Cancela una tarea pendiente de la cola por su ID."""
        tarea_id = self.view.get_id_cancelar()

        if not tarea_id:
            self.view.mostrar_mensaje("⚠ Ingresa el ID de la tarea a cancelar.",
                                      color=self.view.COLOR_MSG_WARN)
            return

        cancelada = self.model.cancelar_tarea(tarea_id)
        if cancelada:
            self.view.limpiar_cancelar()
            self.view.mostrar_mensaje(f"✓ Tarea {tarea_id} cancelada.",
                                      color=self.view.COLOR_MSG_OK)
            self._refrescar()
        else:
            self.view.mostrar_mensaje(
                f"⚠ No se encontró '{tarea_id}' en la cola.",
                color=self.view.COLOR_MSG_ERR
            )

    # ─────────────────────────────────────────
    #  GUARDAR ESTADO
    # ─────────────────────────────────────────
    def guardar_estado(self):
        """Persiste el estado del gestor en el archivo JSON."""
        self.model.guardar_estado(self.archivo_estado)
        self.view.mostrar_mensaje("✓ Estado guardado correctamente.",
                                  color=self.view.COLOR_MSG_OK)

    # ─────────────────────────────────────────
    #  PRIVADO
    # ─────────────────────────────────────────
    def _refrescar(self):
        """Actualiza ambas listas en la vista con los datos actuales del modelo."""
        self.view.actualizar_cola(self.model.ver_cola())
        self.view.actualizar_historial(self.model.historial())