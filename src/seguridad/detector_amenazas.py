"""Reglas de detección didáctica de anomalías simuladas."""
def detectar(procesos, umbral_cpu=80, umbral_memoria=1024):
    alertas = []
    for p in procesos:
        if p.estado == "Terminado":
            continue
        if p.cpu >= umbral_cpu:
            alertas.append({"pid": p.pid, "tipo": "CPU elevada", "detalle": f"{p.cpu}% >= {umbral_cpu}%"})
        if p.memoria >= umbral_memoria:
            alertas.append({"pid": p.pid, "tipo": "Memoria elevada", "detalle": f"{p.memoria} MB >= {umbral_memoria} MB"})
        if "sospechoso" in p.nombre.lower():
            alertas.append({"pid": p.pid, "tipo": "Patrón inusual", "detalle": "Nombre marcado para simulación"})
    return alertas
