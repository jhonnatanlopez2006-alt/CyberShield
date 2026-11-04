from procesos.gestor_procesos import GestorProcesos

def escenario_inicial():
    gestor = GestorProcesos()
    gestor.crear("explorer_demo", cpu=21, memoria_mb=120, prioridad=5)
    gestor.crear("scanner_demo", cpu=91, memoria_mb=450, prioridad=8)
    gestor.crear("service_demo", cpu=4, memoria_mb=60, prioridad=3)
    return gestor.listar()
