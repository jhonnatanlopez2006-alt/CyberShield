"""Modelo y administración segura de procesos ficticios."""
from dataclasses import dataclass, asdict

@dataclass
class Proceso:
    pid: int
    nombre: str
    estado: str
    prioridad: int
    cpu: float
    memoria: float

    def datos(self):
        return asdict(self)

class GestorProcesos:
    def __init__(self):
        self.procesos = {}
        self.siguiente_pid = 1000

    def crear(self, nombre, prioridad=3, cpu=10, memoria=128):
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")
        if not 1 <= int(prioridad) <= 5:
            raise ValueError("La prioridad debe estar entre 1 y 5")
        if not 0 <= float(cpu) <= 100 or float(memoria) < 0:
            raise ValueError("Recursos fuera de rango")
        pid = self.siguiente_pid
        self.siguiente_pid += 1
        proceso = Proceso(pid, nombre.strip(), "Listo", int(prioridad), float(cpu), float(memoria))
        self.procesos[pid] = proceso
        return proceso

    def cambiar_estado(self, pid, accion):
        proceso = self.procesos[int(pid)]
        transiciones = {
            "iniciar": ({"Listo"}, "Ejecución"),
            "pausar": ({"Ejecución"}, "Bloqueado"),
            "reanudar": ({"Bloqueado"}, "Listo"),
            "finalizar": ({"Listo", "Ejecución", "Bloqueado"}, "Terminado"),
        }
        if accion not in transiciones:
            raise ValueError("Acción desconocida")
        permitidos, destino = transiciones[accion]
        if proceso.estado not in permitidos:
            raise ValueError("Transición no permitida desde " + proceso.estado)
        proceso.estado = destino
        return proceso

    def listar(self):
        return list(self.procesos.values())
