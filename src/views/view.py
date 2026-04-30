import tkinter as tk
from tkinter import ttk


class View(tk.Frame):
    # ── Paleta de colores ──────────────────────────────────────────────
    COLOR_BG       = "#ffffff"
    COLOR_PANEL    = "#f5f5f5"
    COLOR_VERDE    = "#83e60a"
    COLOR_OSCURO   = "#24272c"
    COLOR_TEXTO    = "#000000"
    COLOR_BLANCO   = "#ffffff"
    COLOR_GUARDADO = "#37474F"
    COLOR_ROJO     = "#e53935"
    COLOR_AZUL     = "#1565C0"
    COLOR_MSG_OK   = "#83e60a"
    COLOR_MSG_WARN = "#FF6F00"
    COLOR_MSG_ERR  = "#e53935"
    COLOR_MSG_INFO = "#64B5F6"

    def __init__(self, parent):
        super().__init__(parent, bg=self.COLOR_BG)
        self.pack(fill=tk.BOTH, expand=True)
        self._controller = None
        self._build_ui()

    def set_controller(self, controller):
        self._controller = controller

    def _build_ui(self):
        self._build_header()
        contenedor = tk.Frame(self, bg=self.COLOR_BG)
        contenedor.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        contenedor.columnconfigure(1, weight=1)
        contenedor.rowconfigure(0, weight=1)
        self._build_panel_acciones(contenedor)
        self._build_panel_info(contenedor)

    def _build_header(self):
        header = tk.Frame(self, bg=self.COLOR_OSCURO)
        header.pack(fill=tk.X)
        tk.Label(
            header,
            text="GESTOR DE TAREAS - IMPRESORA VIRTUAL",
            bg=self.COLOR_OSCURO,
            fg=self.COLOR_BLANCO,
            font=("Segoe UI", 16, "bold")
        ).pack(pady=12)

    def _build_panel_acciones(self, parent):
        panel = tk.Frame(parent, bg=self.COLOR_PANEL, width=290,
                         highlightbackground="#dddddd", highlightthickness=1)
        panel.grid(row=0, column=0, sticky="ns", padx=(0, 15))
        panel.pack_propagate(False)

        tk.Label(panel, text="NUEVA TAREA", bg=self.COLOR_PANEL,
                 fg=self.COLOR_TEXTO, font=("Segoe UI", 10, "bold")).pack(
                     anchor="w", padx=15, pady=(15, 8))

        # ── Nombre de la tarea ──
        tk.Label(panel, text="Nombre del documento:", bg=self.COLOR_PANEL,
                 fg=self.COLOR_TEXTO, font=("Segoe UI", 9)).pack(anchor="w", padx=15)
        self.input_nombre = tk.Entry(panel, font=("Segoe UI", 10),
                                     bg=self.COLOR_BG, fg=self.COLOR_TEXTO,
                                     insertbackground=self.COLOR_TEXTO,
                                     relief="solid", bd=1)
        self.input_nombre.pack(fill=tk.X, padx=15, pady=(2, 8))

        # ── Tipo de tarea ──
        tk.Label(panel, text="Tipo de tarea:", bg=self.COLOR_PANEL,
                 fg=self.COLOR_TEXTO, font=("Segoe UI", 9)).pack(anchor="w", padx=15)
        self.combo_tipo = ttk.Combobox(
            panel,
            values=["Impresión", "Escaneo", "Copia", "Fax"],
            state="readonly", font=("Segoe UI", 10)
        )
        self.combo_tipo.current(0)
        self.combo_tipo.pack(fill=tk.X, padx=15, pady=(2, 10))

        # ── Botones principales ──
        self._boton(panel, "Agregar tarea",      self.COLOR_VERDE,
                    lambda: self._controller.agregar_tarea())
        self._boton(panel, "Procesar siguiente", self.COLOR_OSCURO,
                    lambda: self._controller.procesar_siguiente())

        ttk.Separator(panel, orient="horizontal").pack(fill=tk.X, padx=15, pady=10)

        # ── Procesamiento por lotes ──
        tk.Label(panel, text="Procesar lote (cantidad):", bg=self.COLOR_PANEL,
                 fg=self.COLOR_TEXTO, font=("Segoe UI", 9)).pack(anchor="w", padx=15)
        self.input_lote = tk.Entry(panel, font=("Segoe UI", 10),
                                   bg=self.COLOR_BG, fg=self.COLOR_TEXTO,
                                   insertbackground=self.COLOR_TEXTO,
                                   relief="solid", bd=1)
        self.input_lote.insert(0, "3")
        self.input_lote.pack(fill=tk.X, padx=15, pady=(2, 6))
        self._boton(panel, "Procesar lote",      self.COLOR_AZUL,
                    lambda: self._controller.procesar_lote())

        ttk.Separator(panel, orient="horizontal").pack(fill=tk.X, padx=15, pady=10)

        # ── Cancelar tarea ──
        tk.Label(panel, text="ID para cancelar (ej: T-003):", bg=self.COLOR_PANEL,
                 fg=self.COLOR_TEXTO, font=("Segoe UI", 9)).pack(anchor="w", padx=15)
        self.input_cancelar = tk.Entry(panel, font=("Segoe UI", 10),
                                       bg=self.COLOR_BG, fg=self.COLOR_TEXTO,
                                       insertbackground=self.COLOR_TEXTO,
                                       relief="solid", bd=1)
        self.input_cancelar.pack(fill=tk.X, padx=15, pady=(2, 6))
        self._boton(panel, "Cancelar tarea",     self.COLOR_ROJO,
                    lambda: self._controller.cancelar_tarea())

        ttk.Separator(panel, orient="horizontal").pack(fill=tk.X, padx=15, pady=10)

        self._boton(panel, "Guardar estado",     self.COLOR_GUARDADO,
                    lambda: self._controller.guardar_estado())

        # ── Mensaje feedback ──
        self.lbl_mensaje = tk.Label(panel, text="", bg=self.COLOR_PANEL,
                                    fg=self.COLOR_MSG_OK,
                                    font=("Segoe UI", 9), wraplength=250)
        self.lbl_mensaje.pack(padx=15, pady=(8, 15))

    def _build_panel_info(self, parent):
        panel = tk.Frame(parent, bg=self.COLOR_BG)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.rowconfigure(0, weight=1)
        panel.rowconfigure(1, weight=1)
        panel.columnconfigure(0, weight=1)

        self._build_lista(panel, "COLA DE TAREAS PENDIENTES", row=0)
        self._build_lista(panel, "HISTORIAL DE TAREAS PROCESADAS", row=1)

    def _build_lista(self, parent, titulo, row):
        frame = tk.Frame(parent, bg=self.COLOR_PANEL,
                         highlightbackground="#dddddd", highlightthickness=1)
        frame.grid(row=row, column=0, sticky="nsew",
                   pady=(0, 10) if row == 0 else 0)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        tk.Label(frame, text=titulo, bg=self.COLOR_PANEL,
                 fg=self.COLOR_TEXTO, font=("Segoe UI", 10, "bold")).grid(
                     row=0, column=0, sticky="w", padx=15, pady=(10, 4))
        ttk.Separator(frame, orient="horizontal").grid(
            row=0, column=0, sticky="ew", padx=15, pady=(35, 0))

        container = tk.Frame(frame, bg=self.COLOR_PANEL)
        container.grid(row=1, column=0, sticky="nsew", padx=15, pady=(5, 10))
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        scrollbar = ttk.Scrollbar(container, orient="vertical")
        lb = tk.Listbox(container, bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO,
                        font=("Segoe UI", 9), relief="flat", bd=0,
                        selectbackground=self.COLOR_VERDE,
                        selectforeground=self.COLOR_OSCURO,
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0)
        scrollbar.config(command=lb.yview)
        lb.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        if "PENDIENTES" in titulo:
            self.lista_cola = lb
        else:
            self.lista_historial = lb

    def _boton(self, parent, texto, color, comando):
        btn = tk.Button(
            parent, text=texto, bg=color,
            fg=self.COLOR_BLANCO,
            activebackground=color,
            activeforeground=self.COLOR_BLANCO,
            font=("Segoe UI", 9, "bold"),
            relief="flat", bd=0, cursor="hand2",
            padx=12, pady=8,
            command=comando
        )
        btn.pack(fill=tk.X, padx=15, pady=3)

    # ─────────────────────────────────────────
    #  MÉTODOS PÚBLICOS
    # ─────────────────────────────────────────
    def mostrar_mensaje(self, texto: str, color: str = None):
        self.lbl_mensaje.config(text=texto, fg=color or self.COLOR_MSG_OK)

    def actualizar_cola(self, cola: list):
        self.lista_cola.delete(0, tk.END)
        if not cola:
            self.lista_cola.insert(tk.END, "  Sin tareas pendientes")
        else:
            for t in cola:
                self.lista_cola.insert(
                    tk.END,
                    f"  {t['id']} | {t['tipo']} | {t['nombre']}"
                )

    def actualizar_historial(self, historial: list):
        self.lista_historial.delete(0, tk.END)
        if not historial:
            self.lista_historial.insert(tk.END, "  Sin tareas procesadas aún")
        else:
            for t in historial:
                self.lista_historial.insert(
                    tk.END,
                    f"  ✓  {t['id']} | {t['tipo']} | {t['nombre']}"
                )

    def get_nombre(self) -> str:
        return self.input_nombre.get().strip()

    def get_tipo(self) -> str:
        return self.combo_tipo.get()

    def get_prioridad(self) -> str:
        return "normal"  # eliminado de la UI, valor fijo por compatibilidad

    def get_lote(self) -> str:
        return self.input_lote.get().strip()

    def get_id_cancelar(self) -> str:
        return self.input_cancelar.get().strip().upper()

    def limpiar_nombre(self):
        self.input_nombre.delete(0, tk.END)

    def limpiar_cancelar(self):
        self.input_cancelar.delete(0, tk.END)