# CyberShield
## Laboratorio de procesos y seguridad informática

CyberShield es un proyecto académico para estudiar conceptos de sistemas operativos y seguridad informática mediante la simulación de procesos, el seguimiento de recursos y la generación de alertas didácticas.

**Aplicación web:** https://jhonnatanlopez2006-alt.github.io/CyberShield/  
**Repositorio:** https://github.com/jhonnatanlopez2006-alt/CyberShield  
**Base de datos y backend:** Supabase

---

## Información del proyecto

| Campo | Descripción |
|---|---|
| Asignatura | Sistemas Operativos |
| Institución | Universidad Manuela Beltrán |
| Autores | Jhonnatan Alexander Lopez Muñoz y Juan Gabriel Gutierrez Trujillo |
| Publicación web | GitHub Pages |
| Backend | Supabase |
| Motor de base de datos | PostgreSQL |

## Objetivo

Construir un entorno de aprendizaje donde se pueda observar el ciclo de vida de procesos, comparar su comportamiento en diferentes escenarios, identificar valores que activan reglas de alerta y consultar el registro de actividad. La aplicación web permite sincronizar información con una base de datos en la nube mediante una sesión autenticada.

## Funcionalidades

### Panel de control
- Resumen de procesos activos, uso simulado de CPU, memoria RAM y alertas.
- Navegación entre las secciones Inicio, Procesos, Alertas y Eventos.
- Actualización de indicadores al realizar acciones en la simulación.

### Gestión de procesos
- Crear procesos ficticios con nombre, prioridad, CPU y memoria.
- Consultar PID, nombre, estado, prioridad y recursos asignados.
- Iniciar, pausar, reanudar y finalizar procesos simulados.
- Observar los cambios de estado durante el ciclo de vida del proceso.

### Escenarios
- **Funcionamiento normal:** carga procesos ficticios con valores moderados.
- **Actividad sospechosa:** introduce un proceso ficticio con características que activan reglas de detección.
- **Personalizado:** permite crear procesos de prueba desde la interfaz.

### Reglas de detección
El dashboard evalúa los datos simulados mediante las siguientes condiciones:

| Regla | Condición |
|---|---|
| Consumo elevado de CPU | CPU mayor o igual a 80 % |
| Memoria elevada | RAM mayor o igual a 1024 MB |
| Nombre sospechoso | El nombre contiene la palabra "sospechoso" |

Estas reglas tienen fines didácticos y no constituyen un motor profesional de detección de amenazas.

### Registro de eventos
- Registra acciones como creación y cambio de estado de procesos, carga de escenarios y análisis.
- Muestra los acontecimientos recientes.
- Permite exportar el registro de eventos disponible en la sesión a un archivo JSON.

## Arquitectura y tecnologías

La aplicación publicada en GitHub Pages es un dashboard web que utiliza Supabase como servicio backend.

| Tecnología o servicio | Responsabilidad |
|---|---|
| HTML5 | Estructura de la interfaz web |
| CSS3 | Diseño y presentación adaptable |
| JavaScript | Lógica de simulación, reglas, alertas, eventos y comunicación con el backend |
| Supabase JS | Cliente para conectar el dashboard con Supabase |
| Supabase Auth | Registro, inicio y cierre de sesión |
| Supabase Database | Servicio de base de datos PostgreSQL |
| PostgreSQL | Motor relacional para organizar y consultar los datos |
| Row Level Security (RLS) | Control de acceso a los registros según el usuario autenticado |
| Git y GitHub | Control de versiones y alojamiento del código fuente |
| GitHub Pages | Publicación de la aplicación web |

### Capas de la aplicación web

1. **Presentación:** interfaz construida con HTML y CSS.
2. **Lógica de aplicación:** JavaScript administra procesos simulados, escenarios, reglas de análisis, alertas y eventos.
3. **Servicios y persistencia:** el cliente de Supabase se comunica con Supabase Auth y PostgreSQL para autenticar usuarios y sincronizar información.

## Base de datos

CyberShield utiliza Supabase Database, basada en PostgreSQL. La definición de tablas, relaciones, índices, permisos y políticas de seguridad se encuentra en [`supabase/schema.sql`](supabase/schema.sql).

La base de datos contiene cuatro tablas principales:

| Tabla | Propósito | Información almacenada |
|---|---|---|
| `cybershield_scenarios` | Escenarios de simulación | Nombre, tipo, fechas y metadatos |
| `cybershield_processes` | Procesos ficticios | PID, nombre, estado, prioridad, CPU y RAM |
| `cybershield_events` | Historial de actividad | Tipo de evento, detalle, fecha y referencias |
| `cybershield_alerts` | Alertas generadas | Tipo, gravedad, descripción, fecha y proceso relacionado |

### Llaves y relaciones

- Cada tabla tiene una llave primaria `id` de tipo UUID.
- `owner_id` referencia al usuario de `auth.users` y asocia los registros con su propietario.
- `scenario_id` relaciona procesos, eventos y alertas con un escenario.
- `process_id`, en eventos y alertas, permite relacionarlos con un registro de proceso.
- `process_pid` conserva el identificador numérico del proceso simulado como dato de referencia.

El PID identifica un proceso dentro de la simulación; no corresponde al identificador de un proceso real del sistema operativo.

### Seguridad de los datos

- RLS está habilitado en las cuatro tablas.
- Las políticas restringen el acceso a las filas cuyo `owner_id` coincide con `auth.uid()`.
- Los permisos distinguen entre lectura, inserción y actualización según la tabla.
- El frontend utiliza una clave publicable y necesita una sesión de Supabase Auth para operar con los datos protegidos.

**Persistencia del dashboard web:** la aplicación recupera el escenario más reciente del usuario y los procesos, eventos y alertas vinculados a ese escenario. Esto no equivale a restaurar automáticamente todos los escenarios históricos. La exportación JSON corresponde al registro de eventos disponible en la sesión de la interfaz.

## Configuración de Supabase

El archivo [`supabase/schema.sql`](supabase/schema.sql) contiene el esquema de la base de datos.

Para configurar una instancia propia:

1. Crear un proyecto en Supabase.
2. Abrir SQL Editor y ejecutar el contenido de `supabase/schema.sql`.
3. Configurar los métodos de autenticación y las URL de redirección según el dominio de publicación.
4. Verificar que la URL y la clave publicable configuradas en el frontend correspondan al proyecto.
5. Crear una cuenta de prueba y comprobar el registro, el inicio de sesión y el aislamiento de datos entre usuarios.

No se deben publicar claves secretas, claves `service_role`, contraseñas ni archivos `.env`. La clave publicable no reemplaza la autenticación ni las políticas RLS.

## Ejecución

### Aplicación web

Abrir la aplicación publicada:

https://jhonnatanlopez2006-alt.github.io/CyberShield/

Para realizar una prueba funcional:

1. Registrarse o iniciar sesión.
2. Ejecutar el escenario normal.
3. Crear o seleccionar un proceso y probar sus acciones.
4. Ejecutar el escenario de actividad sospechosa.
5. Consultar las alertas y el registro de eventos.
6. Comprobar en Supabase los datos asociados al usuario autenticado.

### Prototipo de escritorio Python

El repositorio conserva también un prototipo académico de escritorio basado en Python y Tkinter, organizado en módulos dentro de `src/`. Para preparar el entorno:

```bash
git clone https://github.com/jhonnatanlopez2006-alt/CyberShield.git
cd CyberShield
python -m pip install -r requirements.txt
```

La integración Python/Supabase dispone de documentación y código en `documentacion/integracion_supabase.md` e `integracion/`. La configuración del prototipo de escritorio es independiente del despliegue web.

## Estructura del repositorio

```text
CyberShield/
├── documentacion/                 # Arquitectura, requisitos y guías
│   ├── diagramas/                 # Diagramas de funcionamiento
│   ├── arquitectura_inicial.md
│   ├── descripcion_proyecto.md
│   ├── integracion_supabase.md
│   ├── requerimientos.md
│   └── tecnologias.md
├── integracion/                   # Integración Python con Supabase
├── pruebas/                       # Pruebas automatizadas del prototipo
├── recursos/                      # Recursos del proyecto
├── src/                           # Prototipo modular Python/Tkinter
│   ├── escenarios/
│   ├── eventos/
│   ├── interfaz/
│   ├── procesos/
│   ├── recursos/
│   └── seguridad/
├── supabase/
│   └── schema.sql                 # Esquema PostgreSQL y políticas RLS
├── index.html                     # Aplicación web publicada
├── favicon.svg
├── requirements.txt
├── .env.example
└── README.md
```

## Pruebas del prototipo Python

Para ejecutar las pruebas automatizadas:

```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```

## Documentación adicional

- [Arquitectura inicial](documentacion/arquitectura_inicial.md)
- [Descripción del proyecto](documentacion/descripcion_proyecto.md)
- [Integración con Supabase](documentacion/integracion_supabase.md)
- [Tecnologías](documentacion/tecnologias.md)
- [Requerimientos](documentacion/requerimientos.md)
- [Esquema de base de datos](supabase/schema.sql)

## Alcance y limitaciones

- Los procesos, PID y métricas son datos ficticios.
- Las reglas de alerta son didácticas y no equivalen a detección real de malware.
- La persistencia requiere conexión, sesión válida y políticas RLS configuradas en Supabase.
- La aplicación web y el prototipo Python/Tkinter son componentes distintos dentro del mismo repositorio; sus mecanismos de inicio y configuración no deben confundirse.

## Licencia

Consulta el archivo [LICENSE](LICENSE) para conocer las condiciones de uso y distribución.

---

**CyberShield**  
Laboratorio de procesos y seguridad informática  
Proyecto académico · Universidad Manuela Beltrán
