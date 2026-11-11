"""Cálculo de recursos ficticios, sin consultar el equipo anfitrión."""
def resumen(procesos):
    activos = [p for p in procesos if p.estado != "Terminado"]
    return {
        "cpu_total": round(min(100.0, sum(p.cpu for p in activos)), 2),
        "memoria_total_mb": round(sum(p.memoria for p in activos), 2),
        "procesos_activos": len(activos),
    }
