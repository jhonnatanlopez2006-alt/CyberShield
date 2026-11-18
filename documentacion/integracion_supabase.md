# Integración con Supabase

## Base de datos
Ejecuta el contenido de `supabase/schema.sql` en el SQL Editor del proyecto CyberShield (Project ID: `diksrgovrnlzqomrmlev`). No lo ejecutes en el proyecto Callegold.

## Tablas
- `cybershield_scenarios`: sesiones de simulación.
- `cybershield_processes`: procesos ficticios, estado, prioridad, CPU y RAM simuladas.
- `cybershield_events`: bitácora de acciones.
- `cybershield_alerts`: detecciones didácticas y severidad.

## Variables locales
Copia `.env.example` como `.env` y configura la URL y la clave publicable del proyecto CyberShield. No guardes el archivo `.env` en Git.

## Dependencias
Ejecuta `python -m pip install -r requirements.txt`.

## Seguridad y autenticación
Todas las tablas tienen RLS activado y no aceptan el rol anónimo. Antes de leer o escribir, la app debe autenticar al usuario con Supabase Auth y pasar el access token de la sesión a `SupabaseRepository(access_token=...)`. La clave publicable identifica el proyecto; no reemplaza la autenticación del usuario.

Nunca incluyas claves `sb_secret_...` o `service_role` en `index.html`, scripts públicos, ni en el repositorio.

## Estado de integración
Esta entrega añade el esquema y la capa de persistencia Python, pero no afirma que la base ya esté aplicada ni que la aplicación esté conectada en ejecución. Falta aplicar el SQL en el panel del proyecto y configurar un flujo de inicio de sesión.
