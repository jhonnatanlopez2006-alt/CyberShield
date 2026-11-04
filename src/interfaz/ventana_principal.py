import tkinter as tk
from tkinter import ttk

def iniciar_aplicacion():
    root = tk.Tk()
    root.title("CyberShield - Simulador de procesos")
    root.geometry("900x560")
    root.minsize(720, 440)
    ttk.Label(root, text="CyberShield", font=("Segoe UI", 24, "bold")).pack(pady=(20, 4))
    ttk.Label(root, text="Simulador didáctico de procesos y detección de amenazas").pack()
    ttk.Label(root, text="ENTORNO CONTROLADO · DATOS FICTICIOS", foreground="#16865b").pack(pady=8)
    columns = ("pid", "nombre", "estado", "cpu", "memoria", "prioridad")
    table = ttk.Treeview(root, columns=columns, show="headings", height=12)
    for col, title in zip(columns, ("PID","Proceso","Estado","CPU (%)","Memoria (MB)","Prioridad")):
        table.heading(col, text=title); table.column(col, anchor="center", width=130)
    table.pack(fill="both", expand=True, padx=20, pady=15)
    ttk.Label(root, text="Aún no hay procesos. La simulación permitirá agregarlos durante la demostración.").pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
