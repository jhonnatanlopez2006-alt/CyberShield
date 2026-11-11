"""Pruebas automatizadas sin dependencias externas ni interfaz gráfica."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from procesos.gestor_procesos import GestorProcesos
from recursos.gestor_recursos import resumen
from seguridad.detector_amenazas import detectar
from escenarios.simulador_escenarios import cargar
from eventos.registro_eventos import RegistroEventos

class PruebasCyberShield(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorProcesos()

    def test_creacion_y_estados(self):
        p = self.gestor.crear("editor", 3, 20, 128)
        self.assertEqual(p.estado, "Listo")
        self.gestor.cambiar_estado(p.pid, "iniciar")
        self.gestor.cambiar_estado(p.pid, "pausar")
        self.assertEqual(p.estado, "Bloqueado")
        self.gestor.cambiar_estado(p.pid, "reanudar")
        self.gestor.cambiar_estado(p.pid, "iniciar")
        self.gestor.cambiar_estado(p.pid, "finalizar")
        self.assertEqual(p.estado, "Terminado")

    def test_transicion_invalida(self):
        p = self.gestor.crear("editor")
        with self.assertRaises(ValueError):
            self.gestor.cambiar_estado(p.pid, "pausar")

    def test_recursos(self):
        self.gestor.crear("a", cpu=20, memoria=100)
        self.gestor.crear("b", cpu=30, memoria=200)
        self.assertEqual(resumen(self.gestor.listar())["cpu_total"], 50)
        self.assertEqual(resumen(self.gestor.listar())["memoria_total_mb"], 300)

    def test_escenarios_y_alertas(self):
        cargar(self.gestor, "Normal")
        self.assertEqual(detectar(self.gestor.listar()), [])
        cargar(self.gestor, "Sospechoso")
        self.assertGreaterEqual(len(detectar(self.gestor.listar())), 2)

    def test_persistencia(self):
        with tempfile.TemporaryDirectory() as carpeta:
            registro = RegistroEventos(Path(carpeta) / "eventos.jsonl")
            registro.guardar("prueba", "evento de ejemplo")
            self.assertEqual(registro.leer()[0]["tipo"], "prueba")

if __name__ == "__main__":
    unittest.main()
