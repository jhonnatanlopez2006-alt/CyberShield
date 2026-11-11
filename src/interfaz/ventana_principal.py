"""CyberShield Fase II: dashboard profesional de monitoreo SIMULADO con Tkinter."""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from procesos.gestor_procesos import GestorProcesos
from recursos.gestor_recursos import resumen
from seguridad.detector_amenazas import detectar
from eventos.registro_eventos import RegistroEventos
from escenarios.simulador_escenarios import cargar

BG = "#090F1E"
PANEL = "#111C30"
PANEL2 = "#17253C"
BORDER = "#283954"
TEXT = "#E8F1FF"
MUTED = "#91A5C0"
CYAN = "#36D6E7"
GREEN = "#43D9A3"
RED = "#FF7285"
AMBER = "#FFC46B"

class VentanaPrincipal:
    def __init__(self):
        self.gestor = GestorProcesos()
        self.registro = RegistroEventos()
        self.root = tk.Tk()
        self.root.title("CyberShield  |  Security Operations Dashboard")
        self.root.geometry("1220x790")
        self.root.minsize(980, 650)
        self.root.configure(bg=BG)
        self.alertas = []
        self.pagina = "Dashboard"
        self._estilos()
        self._estructura()
        self.actualizar()

    def _estilos(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("Cyber.Treeview", background=PANEL, fieldbackground=PANEL,
                        foreground=TEXT, borderwidth=0, rowheight=36,
                        font=("Segoe UI", 10))
        style.configure("Cyber.Treeview.Heading", background=PANEL2, foreground=MUTED,
                        font=("Segoe UI", 9, "bold"), relief="flat", padding=(8, 12))
        style.map("Cyber.Treeview", background=[("selected", "#24566A")],
                  foreground=[("selected", "#FFFFFF")])
        style.map("Cyber.Treeview.Heading", background=[("active", PANEL2)])
        style.configure("Cyber.Vertical.TScrollbar", background=PANEL2,
                        troughcolor=PANEL, arrowcolor=TEXT)

    def _label(self, parent, text, size=11, color=TEXT, bold=False, **kwargs):
        return tk.Label(parent, text=text, bg=parent.cget("bg"), fg=color,
                        font=("Segoe UI", size, "bold" if bold else "normal"), **kwargs)

    def _button(self, parent, text, command, color=CYAN, fg=BG, width=None):
        return tk.Button(parent, text=text, command=command, bg=color, fg=fg,
                         activebackground="#5CE8F0" if color == CYAN else PANEL2,
                         activeforeground=fg, relief="flat", bd=0, cursor="hand2",
                         font=("Segoe UI", 10, "bold"), padx=14, pady=10,
                         width=width, highlightthickness=0)

    def _estructura(self):
        outer = tk.Frame(self.root, bg=BG)
        outer.pack(fill="both", expand=True)
        side = tk.Frame(outer, bg=PANEL, width=218)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)
        tk.Label(side, text="◈  CYBERSHIELD", bg=PANEL, fg=CYAN,
                 font=("Segoe UI", 17, "bold")).pack(anchor="w", padx=20, pady=(27, 2))
        tk.Label(side, text="SECURITY OPERATIONS", bg=PANEL, fg=MUTED,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=22, pady=(0, 35))
        for nombre, icono in [("Dashboard", "▦"), ("Procesos", "≡"),
                              ("Alertas", "⚑"), ("Eventos", "◷")]:
            tk.Button(side, text=f"  {icono}    {nombre}", anchor="w",
                      command=lambda n=nombre: self.navegar(n),
                      bg=PANEL2 if nombre == "Dashboard" else PANEL,
                      fg=CYAN if nombre == "Dashboard" else TEXT,
                      activebackground=PANEL2, activeforeground=CYAN,
                      relief="flat", bd=0, padx=18, pady=15,
                      font=("Segoe UI", 11), cursor="hand2").pack(fill="x", padx=10, pady=3)
        tk.Label(side, text="●  SIMULACIÓN SEGURA", bg=PANEL, fg=GREEN,
                 font=("Segoe UI", 9, "bold")).pack(side="bottom", pady=25)
        self.area = tk.Frame(outer, bg=BG)
        self.area.pack(side="left", fill="both", expand=True, padx=28, pady=22)
        top = tk.Frame(self.area, bg=BG)
        top.pack(fill="x")
        left = tk.Frame(top, bg=BG)
        left.pack(side="left")
        self.titulo = self._label(left, "Panel de control", 23, TEXT, True)
        self.titulo.pack(anchor="w")
        self._label(left, "Monitoreo y análisis de procesos ficticios en tiempo real",
                    10, MUTED).pack(anchor="w", pady=(2, 0))
        self._label(top, "● ENTORNO CONTROLADO", 10, GREEN, True).pack(side="right")
        cards = tk.Frame(self.area, bg=BG)
        cards.pack(fill="x", pady=(24, 22))
        self.cards = {}
        for key, title, accent in [("procesos", "PROCESOS ACTIVOS", CYAN),
                                    ("cpu", "CPU SIMULADA", GREEN),
                                    ("memoria", "MEMORIA SIMULADA", AMBER),
                                    ("alertas", "ALERTAS DETECTADAS", RED)]:
            card = tk.Frame(cards, bg=PANEL, highlightbackground=BORDER,
                            highlightthickness=1, padx=16, pady=15)
            card.pack(side="left", fill="both", expand=True, padx=(0, 10))
            self._label(card, title, 9, MUTED, True).pack(anchor="w")
            value = self._label(card, "—", 25, accent, True)
            value.pack(anchor="w", pady=(9, 0))
            self.cards[key] = value
        actions = tk.Frame(self.area, bg=BG)
        actions.pack(fill="x", pady=(0, 14))
        self._label(actions, "Gestión de procesos", 15, TEXT, True).pack(side="left")
        self._button(actions, "+ Nuevo proceso", self.crear).pack(side="right")
        toolbar = tk.Frame(self.area, bg=BG)
        toolbar.pack(fill="x", pady=(0, 14))
        for title, callback in [
            ("▶ Iniciar", lambda: self.estado("iniciar")),
            ("Ⅱ Pausar", lambda: self.estado("pausar")),
            ("↻ Reanudar", lambda: self.estado("reanudar")),
            ("■ Finalizar", lambda: self.estado("finalizar")),
        ]:
            self._button(toolbar, title, callback, PANEL2, TEXT).pack(side="left", padx=(0, 8))
        self._button(toolbar, "⚠ Analizar", self.analizar, "#6B3547", TEXT).pack(side="right")
        frame = tk.Frame(self.area, bg=PANEL, highlightbackground=BORDER,
                         highlightthickness=1)
        frame.pack(fill="both", expand=True)
        columns = ("pid", "nombre", "estado", "prioridad", "cpu", "memoria")
        self.tabla = ttk.Treeview(frame, columns=columns, show="headings",
                                  style="Cyber.Treeview", selectmode="browse")
        for col, title, ancho in [
            ("pid", "PID", 70), ("nombre", "PROCESO", 190),
            ("estado", "ESTADO", 110), ("prioridad", "PRIORIDAD", 100),
            ("cpu", "CPU (%)", 100), ("memoria", "RAM (MB)", 110),
        ]:
            self.tabla.heading(col, text=title)
            self.tabla.column(col, width=ancho, minwidth=60, anchor="center" if col != "nombre" else "w")
        self.tabla.tag_configure("alerta", foreground=RED)
        self.tabla.tag_configure("terminado", foreground=MUTED)
        self.tabla.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tabla.yview,
                               style="Cyber.Vertical.TScrollbar")
        scroll.pack(side="right", fill="y")
        self.tabla.configure(yscrollcommand=scroll.set)
        bottom = tk.Frame(self.area, bg=BG)
        bottom.pack(fill="x", pady=(17, 0))
        self._label(bottom, "ESCENARIOS DE DEMOSTRACIÓN", 9, MUTED, True).pack(side="left")
        self._button(bottom, "Escenario normal", lambda: self.escenario("Normal"),
                     PANEL2, TEXT).pack(side="left", padx=(14, 8))
        self._button(bottom, "Escenario sospechoso", lambda: self.escenario("Sospechoso"),
                     "#6B3547", TEXT).pack(side="left")
        log_frame = tk.Frame(self.area, bg=PANEL, highlightbackground=BORDER,
                             highlightthickness=1)
        log_frame.pack(fill="x", pady=(14, 0))
        self._label(log_frame, "  CONSOLA DE EVENTOS", 9, MUTED, True).pack(anchor="w", pady=(9, 3))
        self.salida = tk.Text(log_frame, height=5, bg=PANEL, fg=GREEN,
                              insertbackground=TEXT, relief="flat", bd=0,
                              font=("Consolas", 10), padx=14, pady=5, state="disabled")
        self.salida.pack(fill="x")
        self.mensaje("CyberShield iniciado. Los datos mostrados son simulados.")

    def navegar(self, nombre):
        self.pagina = nombre
        titulos = {"Dashboard": "Panel de control", "Procesos": "Gestión de procesos",
                   "Alertas": "Centro de alertas", "Eventos": "Registro de eventos"}
        self.titulo.configure(text=titulos[nombre])
        if nombre == "Alertas":
            self.analizar()
        elif nombre == "Eventos":
            eventos = self.registro.leer()
            self.mensaje(f"Historial: {len(eventos)} eventos almacenados.")
            for evento in eventos[-8:]:
                self.mensaje(f"{evento['fecha']} | {evento['tipo']} | {evento['detalle']}")
        elif nombre == "Procesos":
            self.mensaje("Selecciona una fila y utiliza los controles para administrar el proceso.")

    def mensaje(self, texto):
        self.salida.configure(state="normal")
        self.salida.insert("end", "› " + texto + "\n")
        self.salida.see("end")
        self.salida.configure(state="disabled")

    def actualizar(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        procesos = self.gestor.listar()
        alertas = detectar(procesos)
        pids_alerta = {a["pid"] for a in alertas}
        for p in procesos:
            tag = "terminado" if p.estado == "Terminado" else "alerta" if p.pid in pids_alerta else ""
            self.tabla.insert("", "end",
                              values=(p.pid, p.nombre, p.estado, p.prioridad,
                                      f"{p.cpu:.1f}", f"{p.memoria:.1f}"),
                              tags=(tag,))
        r = resumen(procesos)
        self.cards["procesos"].configure(text=str(r["procesos_activos"]))
        self.cards["cpu"].configure(text=f'{r["cpu_total"]:.1f}%')
        self.cards["memoria"].configure(text=f'{r["memoria_total_mb"]:.0f} MB')
        self.cards["alertas"].configure(text=str(len(alertas)))

    def crear(self):
        nombre = simpledialog.askstring("Nuevo proceso", "Nombre del proceso ficticio:", parent=self.root)
        if nombre is None:
            return
        try:
            p = self.gestor.crear(nombre)
            self.registro.guardar("creación", f"PID {p.pid}: {p.nombre}")
            self.mensaje(f"Proceso creado: {p.nombre} (PID {p.pid})")
            self.actualizar()
        except ValueError as exc:
            messagebox.showerror("Datos inválidos", str(exc), parent=self.root)

    def estado(self, accion):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showinfo("Selecciona un proceso", "Primero selecciona una fila de la tabla.", parent=self.root)
            return
        pid = int(self.tabla.item(seleccion[0], "values")[0])
        try:
            p = self.gestor.cambiar_estado(pid, accion)
            self.registro.guardar("estado", f"PID {pid}: {accion} -> {p.estado}")
            self.mensaje(f"PID {pid}: {p.estado}")
            self.actualizar()
        except (ValueError, KeyError) as exc:
            messagebox.showerror("Transición no permitida", str(exc), parent=self.root)

    def escenario(self, nombre):
        cargar(self.gestor, nombre)
        self.registro.guardar("escenario", nombre)
        self.mensaje(f"Escenario «{nombre}» cargado correctamente.")
        self.actualizar()
        self.analizar()

    def analizar(self):
        self.alertas = detectar(self.gestor.listar())
        if not self.alertas:
            self.mensaje("Análisis finalizado: sin anomalías simuladas.")
        for alerta in self.alertas:
            detalle = f"PID {alerta['pid']} | {alerta['tipo']}: {alerta['detalle']}"
            self.registro.guardar("alerta", detalle)
            self.mensaje("⚠ " + detalle)
        self.actualizar()

    def ejecutar(self):
        self.root.mainloop()
