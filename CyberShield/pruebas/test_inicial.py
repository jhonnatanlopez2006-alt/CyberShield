import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from procesos.gestor_procesos import GestorProcesos
from seguridad.detector_amenazas import DetectorAmenazas

def test_crear_proceso():
    proceso = GestorProcesos().crear("demo", cpu=10, memoria_mb=64)
    assert proceso.nombre == "demo"
    assert proceso.estado == "Listo"

def test_alerta_cpu_alta():
    proceso = GestorProcesos().crear("demo", cpu=95, memoria_mb=100)
    assert DetectorAmenazas().analizar(proceso)
