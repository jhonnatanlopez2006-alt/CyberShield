"""Acceso opcional a Supabase para CyberShield.

La simulación sigue funcionando sin conexión. Las escrituras en la nube
requieren una sesión autenticada de Supabase Auth y variables de entorno.
"""
import os

try:
    from supabase import create_client
except ImportError:
    create_client = None


class SupabaseRepository:
    def __init__(self, url=None, key=None, access_token=None):
        self.url = url or os.getenv("SUPABASE_URL")
        self.key = key or os.getenv("SUPABASE_PUBLISHABLE_KEY")
        if not self.url or not self.key:
            raise RuntimeError("Configura SUPABASE_URL y SUPABASE_PUBLISHABLE_KEY.")
        if create_client is None:
            raise RuntimeError("Instala las dependencias con: pip install -r requirements.txt")
        self.client = create_client(self.url, self.key)
        if access_token:
            self.client.postgrest.auth(access_token)

    def crear_escenario(self, nombre, tipo):
        payload = {"name": nombre, "scenario_type": tipo}
        return self.client.table("cybershield_scenarios").insert(payload).execute().data

    def guardar_proceso(self, proceso, scenario_id=None):
        payload = {
            "scenario_id": scenario_id,
            "pid": int(proceso.pid),
            "name": proceso.nombre,
            "state": proceso.estado,
            "priority": int(proceso.prioridad),
            "cpu_percent": float(proceso.cpu),
            "memory_mb": float(proceso.memoria),
        }
        return self.client.table("cybershield_processes").insert(payload).execute().data

    def registrar_evento(self, tipo, detalle, scenario_id=None, process_pid=None):
        payload = {
            "scenario_id": scenario_id,
            "process_pid": process_pid,
            "event_type": tipo,
            "details": detalle,
        }
        return self.client.table("cybershield_events").insert(payload).execute().data

    def registrar_alerta(self, tipo, gravedad, descripcion, scenario_id=None, process_pid=None):
        payload = {
            "scenario_id": scenario_id,
            "process_pid": process_pid,
            "alert_type": tipo,
            "severity": gravedad,
            "description": descripcion,
        }
        return self.client.table("cybershield_alerts").insert(payload).execute().data

    def listar_procesos(self, limite=100):
        return self.client.table("cybershield_processes").select("*").order("created_at", desc=True).limit(limite).execute().data

    def listar_eventos(self, limite=100):
        return self.client.table("cybershield_events").select("*").order("occurred_at", desc=True).limit(limite).execute().data
