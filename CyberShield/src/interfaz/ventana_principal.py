import tkinter as tk
from tkinter import ttk

def iniciar_aplicacion():
    root = tk.Tk()
    root.title("CyberShield - Simulador de procesos")
    root.geometry("900x560")
    root.minsize(720, 440)

    ttk.Label(root, text="CyberShield", font=("Segoe UI", 24, "bold")).pack(pady=(20, 4))
    ttk.Label(root, text="Simulador didáctico de procesos y detección de amenazas").pack()
    ttk.Label(root, text="DEMO CONTROLADA · DATOS FICTICIOS", foreground="#16865b").pack(pady=8)

    columns = ("pid", "nombre", "estado", "cpu", "memoria", "prioridad")
    table = ttk.Treeview(root, columns=columns, show="headings", height=12)
    labels = ("PID", "Proceso", "Estado", "CPU (%)", "Memoria (MB)", "Prioridad")
    for col, label in zip(columns, labels):
        table.heading(col, text=label)
        table.column(col, anchor="center", width=130)
    table.pack(fill="both", expand=True, padx=20, pady=15)

    for row in [
        (1012, "explorer_demo", "En ejecución", "21%", "120 MB", "Normal"),
        (2048, "scanner_demo", "Sospechoso", "67%", "450 MB", "Alta"),
        (3076, "service_demo", "Listo", "4%", "60 MB", "Baja"),
    ]:
        table.insert("", "end", values=row)

    ttk.Label(root, text="Los datos son simulados. No se inspeccionan ni modifican procesos reales.").pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
