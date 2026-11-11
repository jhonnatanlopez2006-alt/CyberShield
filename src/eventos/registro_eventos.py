"""Persistencia local de eventos en JSON Lines."""
import json
from datetime import datetime
from pathlib import Path

class RegistroEventos:
    def __init__(self, ruta=None):
        self.ruta = Path(ruta) if ruta else Path(__file__).resolve().parents[2] / "registros" / "eventos.jsonl"

    def guardar(self, tipo, detalle):
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        evento = {"fecha": datetime.now().isoformat(timespec="seconds"), "tipo": tipo, "detalle": detalle}
        with self.ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(json.dumps(evento, ensure_ascii=False) + "\n")
        return evento

    def leer(self):
        if not self.ruta.exists():
            return []
        with self.ruta.open(encoding="utf-8") as archivo:
            return [json.loads(linea) for linea in archivo if linea.strip()]
