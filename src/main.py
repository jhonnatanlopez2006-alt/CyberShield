"""Punto de entrada de CyberShield Fase II (Python 3.10+)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except ImportError:
    pass

from interfaz.ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    VentanaPrincipal().ejecutar()
