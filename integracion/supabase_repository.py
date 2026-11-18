"""Persistencia autenticada de CyberShield en Supabase.

Usa la clave publicable del proyecto y una sesión de Supabase Auth.
No almacena credenciales en el repositorio.
"""
import os

try:
    from supabase import create_client
except ImportError:
    create_client = None


class SupabaseRepository:
    def __init__(self, url=None, key=None):
        self.url = url or os.getenv("SUPABASE_URL")
        self.key = key or os.getenv("SUPABASE_PUBLISHABLE_KEY")
        if not self.url or not self.key:
            raise RuntimeError("Configura SUPABASE_URL y SUPABASE_PUBLISHABLE_KEY.")
        if create_client is None:
            raise RuntimeError("Instala dependencias con: pip install -r requirements.txt")
        self.client = create_client(self.url, self.key)
        self.user_id = None
        self.scenario_id = None

    def iniciar_sesion(self, correo, contrasena):
        """Autentica con Supabase Auth; RLS limita los datos al usuario."""
        response = self.client.auth.sign_in_with_password(
            {"email": correo, "password": contrasena}
        )
        if not response.user or not response.session:
            raise RuntimeError("Supabase Auth no devolvió una sesión válida.")
        self.user_id = response.user.id
        return response.user

    def cerrar_sesion(self):
        self.client.auth.sign_out()
        self.user_id = None
        self.scenario_id = None

    def _require_auth(self):
        if not self.user_id:
            raise RuntimeError("Inicia sesión en Supabase Auth antes de guardar datos.")

    def crear_escenario(self, nombre, tipo):
        self._require_auth()
        payload = {"name": nombre, "scenario_type": tipo}
        result = self.client.table("cybershield_scenarios").insert(payload).execute()
        self.scenario_id = result.data[0]["id"] if result.data else None
        return result.data

    def guardar_proceso(self, proceso):
        self._require_auth()
        payload = {
            "scenario_id": self.scenario_id,
            "pid": int(proceso.pid),
            "name": proceso.nombre,
            "state": proceso.estado,
            "priority": int(proceso.prioridad),
            "cpu_percent": float(proceso.cpu),
            "memory_mb": float(proceso.memoria),
        }
        return self.client.table("cybershield_processes").upsert(
            payload, on_conflict="owner_id,pid"
        ).execute().data

    def registrar_evento(self, tipo, detalle, process_pid=None):
        self._require_auth()
        payload = {
            "scenario_id": self.scenario_id,
            "process_pid": process_pid,
            "event_type": tipo,
            "details": detalle,
        }
        return self.client.table("cybershield_events").insert(payload).execute().data

    def registrar_alerta(self, tipo, gravedad, descripcion, process_pid=None):
        self._require_auth()
        payload = {
            "scenario_id": self.scenario_id,
            "process_pid": process_pid,
            "alert_type": tipo,
            "severity": gravedad,
            "description": descripcion,
        }
        return self.client.table("cybershield_alerts").insert(payload).execute().data

    def listar_procesos(self, limite=100):
        self._require_auth()
        return (self.client.table("cybershield_processes").select("*")
                .order("created_at", desc=True).limit(limite).execute().data)

    def listar_eventos(self, limite=100):
        self._require_auth()
        return (self.client.table("cybershield_events").select("*")
                .order("occurred_at", desc=True).limit(limite).execute().data)
