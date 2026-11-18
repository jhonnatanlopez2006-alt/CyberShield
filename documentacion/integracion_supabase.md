# Integración con Supabase

## Base de datos
Las tablas de CyberShield son `cybershield_scenarios`, `cybershield_processes`, `cybershield_events` y `cybershield_alerts`. Ejecuta el contenido actualizado de `supabase/schema.sql` en el SQL Editor del proyecto CyberShield. Es compatible con las tablas creadas en la primera ejecución: agrega `owner_id`, índices y políticas por usuario sin borrar tablas.

## Configuración local
Copia `.env.example` como `.env` y configura la URL y la clave publicable. El archivo `.env` está excluido por Git.

## Cuenta de acceso
En Supabase Dashboard → Authentication → Users, crea una cuenta de usuario con correo y contraseña. La app de escritorio solicitará esas credenciales al iniciar si la configuración de Supabase existe. No escribas la contraseña en el código ni en el repositorio.

## Seguridad
Todas las tablas tienen RLS y cada fila pertenece al usuario autenticado mediante `owner_id = auth.uid()`. La clave publicable no autentica al usuario por sí sola; se requiere una sesión de Supabase Auth. No uses claves `sb_secret_...` ni `service_role` en clientes públicos o escritorio.

## Modo sin conexión
Si no existe configuración, no se puede iniciar sesión o Supabase no está disponible, el simulador conserva su operación local y el registro JSONL. Los datos locales no se sincronizan retroactivamente de forma automática.
