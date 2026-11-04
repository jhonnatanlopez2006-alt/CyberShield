from dataclasses import dataclass
from itertools import count
_ids = count(1000)

@dataclass
class ProcesoSimulado:
    pid: int
    nombre: str
    estado: str = "Listo"
    cpu: float = 0.0
    memoria_mb: int = 0
    prioridad: int = 5

class GestorProcesos:
    """Administra procesos ficticios dentro de la simulación."""
    def __init__(self):
        self.procesos = {}
    def crear(self, nombre, cpu=0.0, memoria_mb=0, prioridad=5):
        p = ProcesoSimulado(next(_ids), nombre, "Listo", cpu, memoria_mb, prioridad)
        self.procesos[p.pid] = p
        return p
    def listar(self):
        return list(self.procesos.values())
    def cambiar_estado(self, pid, estado):
        permitidos = {"Listo", "Ejecución", "Bloqueado", "Terminado"}
        if estado not in permitidos:
            raise ValueError("Estado no válido")
        self.procesos[pid].estado = estado
        return self.procesos[pid]
