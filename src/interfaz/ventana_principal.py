"""Interfaz gráfica Tkinter del simulador CyberShield."""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from procesos.gestor_procesos import GestorProcesos
from recursos.gestor_recursos import resumen
from seguridad.detector_amenazas import detectar
from eventos.registro_eventos import RegistroEventos
from escenarios.simulador_escenarios import cargar

class VentanaPrincipal:
    def __init__(self):
        self.gestor = GestorProcesos()
        self.registro = RegistroEventos()
        self.root = tk.Tk()
        self.root.title("CyberShield | Simulador de procesos")
        self.root.geometry("940x620")
        ttk.Label(self.root, text="CyberShield - Fase II", font=("Arial", 19, "bold")).pack(pady=12)
        ttk.Label(self.root, text="Entorno didáctico: todos los procesos y recursos son simulados").pack()
        barra = ttk.Frame(self.root)
        barra.pack(pady=12)
        for texto, accion in [
            ("Crear proceso", self.crear), ("Iniciar", lambda: self.estado("iniciar")),
            ("Pausar", lambda: self.estado("pausar")), ("Reanudar", lambda: self.estado("reanudar")),
            ("Finalizar", lambda: self.estado("finalizar")),
            ("Escenario normal", lambda: self.escenario("Normal")),
            ("Escenario sospechoso", lambda: self.escenario("Sospechoso")),
            ("Analizar alertas", self.analizar),
        ]:
            ttk.Button(barra, text=texto, command=accion).pack(side="left", padx=3)
        columnas = ("pid", "nombre", "estado", "prioridad", "cpu", "memoria")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings", height=13)
        for col, ancho in zip(columnas, (70, 220, 130, 90, 100, 110)):
            self.tabla.heading(col, text=col.upper())
            self.tabla.column(col, width=ancho)
        self.tabla.pack(fill="both", expand=True, padx=16)
        self.estadisticas = ttk.Label(self.root, text="")
        self.estadisticas.pack(pady=8)
        ttk.Label(self.root, text="Eventos y alertas").pack()
        self.salida = tk.Text(self.root, height=7, state="disabled")
        self.salida.pack(fill="x", padx=16, pady=8)
        self.actualizar()

    def mensaje(self, texto):
        self.salida.configure(state="normal")
        self.salida.insert("end", texto + "\n")
        self.salida.see("end")
        self.salida.configure(state="disabled")

    def actualizar(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for p in self.gestor.listar():
            self.tabla.insert("", "end", values=(p.pid, p.nombre, p.estado, p.prioridad, p.cpu, p.memoria))
        r = resumen(self.gestor.listar())
        self.estadisticas.configure(text=f"CPU simulada: {r['cpu_total']}%  |  Memoria simulada: {r['memoria_total_mb']} MB  |  Activos: {r['procesos_activos']}")

    def crear(self):
        nombre = simpledialog.askstring("Nuevo proceso", "Nombre del proceso:", parent=self.root)
        if nombre is None:
            return
        try:
            p = self.gestor.crear(nombre)
            self.registro.guardar("creación", f"PID {p.pid}: {p.nombre}")
            self.mensaje(f"Proceso ficticio creado: {p.pid}")
            self.actualizar()
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def estado(self, accion):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showinfo("Seleccionar", "Selecciona un proceso de la tabla")
            return
        pid = int(self.tabla.item(seleccion[0], "values")[0])
        try:
            p = self.gestor.cambiar_estado(pid, accion)
            self.registro.guardar("estado", f"PID {pid}: {accion} -> {p.estado}")
            self.mensaje(f"PID {pid}: {p.estado}")
            self.actualizar()
        except (ValueError, KeyError) as exc:
            messagebox.showerror("Transición inválida", str(exc))

    def escenario(self, nombre):
        cargar(self.gestor, nombre)
        self.registro.guardar("escenario", nombre)
        self.mensaje(f"Escenario {nombre} cargado")
        self.actualizar()
        self.analizar()

    def analizar(self):
        alertas = detectar(self.gestor.listar())
        if not alertas:
            self.mensaje("Análisis: sin anomalías simuladas")
        for alerta in alertas:
            detalle = f"PID {alerta['pid']}: {alerta['tipo']} - {alerta['detalle']}"
            self.registro.guardar("alerta", detalle)
            self.mensaje("ALERTA: " + detalle)

    def ejecutar(self):
        self.root.mainloop()
