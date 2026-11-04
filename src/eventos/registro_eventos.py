import json
from datetime import datetime, timezone
from pathlib import Path

class RegistroEventos:
    def __init__(self, ruta="eventos.json"):
        self.ruta = Path(ruta)
    def consultar(self):
        if not self.ruta.exists():
            return []
        return json.loads(self.ruta.read_text(encoding="utf-8"))
    def registrar(self, mensaje, tipo="INFO"):
        eventos = self.consultar()
        eventos.append({
            "fecha": datetime.now(timezone.utc).isoformat(),
            "tipo": tipo,
            "mensaje": mensaje
        })
        self.ruta.write_text(json.dumps(eventos, ensure_ascii=False, indent=2), encoding="utf-8")
