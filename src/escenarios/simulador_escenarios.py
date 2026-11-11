"""Escenarios reproducibles con datos ficticios."""
ESCENARIOS = {
    "Normal": [
        ("editor", 3, 12, 160),
        ("navegador", 2, 25, 380),
        ("servicio", 4, 8, 90),
    ],
    "Sospechoso": [
        ("editor", 3, 15, 180),
        ("proceso_sospechoso", 1, 95, 1500),
        ("servicio", 4, 9, 100),
    ],
}

def cargar(gestor, nombre):
    if nombre not in ESCENARIOS:
        raise ValueError("Escenario no encontrado")
    gestor.procesos.clear()
    return [gestor.crear(*datos) for datos in ESCENARIOS[nombre]]
