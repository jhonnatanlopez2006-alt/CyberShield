class GestorRecursos:
    def resumir(self, procesos):
        return {
            "cpu_total": round(sum(p.cpu for p in procesos), 2),
            "memoria_total_mb": sum(p.memoria_mb for p in procesos),
            "cantidad_procesos": len(procesos),
        }
