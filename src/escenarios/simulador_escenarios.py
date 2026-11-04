"""Funciones de escenarios; los datos solo se crean cuando se invocan."""
from procesos.gestor_procesos import GestorProcesos

def crear_escenario_normal():
    gestor = GestorProcesos()
    gestor.crear("proceso_normal_demo", cpu=12.0, memoria_mb=120)
    return gestor.listar()
