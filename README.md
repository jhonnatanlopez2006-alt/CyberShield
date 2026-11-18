# 🛡️ CyberShield
### Laboratorio de procesos y seguridad informática

**CyberShield** es un proyecto académico que permite explorar conceptos de sistemas operativos y seguridad informática mediante la simulación de procesos, el seguimiento de recursos y la generación de alertas didácticas.

<p align="center">
  <a href="https://jhonnatanlopez2006-alt.github.io/CyberShield/"><strong>🌐 Abrir aplicación web</strong></a>
  ·
  <a href="https://supabase.com/dashboard/project/diksrgovrnlzqomrmlev"><strong>🗄️ Proyecto Supabase</strong></a>
</p>

> [!IMPORTANT]
> CyberShield es un **simulador educativo**. Los procesos, PID, consumo de CPU y memoria son datos ficticios. La aplicación no inspecciona, modifica, detiene ni elimina procesos reales del computador y no ejecuta malware. No es un antivirus ni una herramienta de protección en tiempo real.

---

## 📌 Información del proyecto

| Dato | Descripción |
|---|---|
| Proyecto | CyberShield |
| Asignatura | Sistemas Operativos |
| Institución | Universidad Manuela Beltrán |
| Autores | Jhonnatan Alexander Lopez Muñoz y Juan Gabriel Gutierrez Trujillo |
| Aplicación publicada | [GitHub Pages](https://jhonnatanlopez2006-alt.github.io/CyberShield/) |
| Repositorio | [GitHub](https://github.com/jhonnatanlopez2006-alt/CyberShield) |
| Backend y base de datos | [Supabase](https://supabase.com/) |

## 🎯 Objetivo

Construir un entorno de aprendizaje donde el estudiante pueda observar el ciclo de vida de procesos, comparar su comportamiento en diferentes escenarios, reconocer valores que activan reglas de alerta y consultar el registro de actividad. La información de la aplicación web puede sincronizarse con una base de datos en la nube asociada al usuario autenticado.

## ✨ Funcionalidades principales

### Panel de control
- Resumen de procesos activos, uso simulado de CPU, memoria RAM y alertas.
- Navegación entre Inicio, Procesos, Alertas y Eventos.
- Indicadores que se actualizan al realizar acciones en la simulación.

### Gestión de procesos
- Crear procesos ficticios con nombre, prioridad, CPU y memoria.
- Consultar el PID, nombre, estado, prioridad y recursos asignados.
- Iniciar, pausar, reanudar y finalizar procesos simulados.
- Visualizar los cambios de estado durante el ciclo de vida del proceso.

### Escenarios de simulación
- **Funcionamiento normal:** carga procesos cotidianos con valores moderados.
- **Actividad sospechosa:** introduce un proceso ficticio con características que permiten activar las reglas de detección.
- **Escenario personalizado:** permite crear procesos de prueba desde la interfaz.

### Reglas y alertas didácticas
El dashboard aplica reglas sencillas sobre los datos simulados:

| Regla | Condición ilustrativa |
|---|---|
| Consumo elevado de CPU | CPU mayor o igual a 80 % |
| Memoria elevada | RAM mayor o igual a 1024 MB |
| Nombre sospechoso | El nombre contiene la palabra «sospechoso» |

Las reglas permiten explicar cómo un sistema puede evaluar indicadores y producir alertas. No representan un motor profesional de detección de amenazas.

### Registro de eventos
- Registra acciones como creación y cambio de estado de procesos, carga de escenarios y análisis.
- Muestra los acontecimientos recientes en la interfaz.
- Permite exportar el registro de eventos de la sesión a un archivo JSON.

## 🧩 Arquitectura y tecnologías

La solución publicada en GitHub Pages es un dashboard web estático que utiliza Supabase como servicio backend.

| Tecnología / servicio | Responsabilidad |
|---|---|
| HTML5 | Estructura de la interfaz web |
| CSS3 | Diseño visual adaptable y estilos |
| JavaScript | Lógica de simulación, reglas, eventos y comunicación con el backend |
| Supabase JS | Cliente que conecta el dashboard con Supabase |
| Supabase Auth | Registro, inicio y cierre de sesión de usuarios |
| Supabase Database | Servicio PostgreSQL para persistencia de información |
| PostgreSQL | Motor relacional que organiza los datos en tablas |
| Row Level Security (RLS) | Políticas de acceso a los registros según el usuario autenticado |
| Git y GitHub | Control de versiones y alojamiento del código fuente |
| GitHub Pages | Publicación de la aplicación web |

### Capas de la aplicación web

1. **Presentación:** interfaz HTML y CSS, con las vistas del dashboard.
2. **Lógica de aplicación:** JavaScript administra procesos simulados, escenarios, reglas de análisis, alertas y eventos.
3. **Servicios y persistencia:** el cliente Supabase se comunica con Supabase Auth y PostgreSQL para autenticar usuarios y sincronizar información.

## 🗄️ Base de datos

CyberShield utiliza **Supabase Database**, basada en PostgreSQL. El esquema se encuentra en [`supabase/schema.sql`](supabase/schema.sql).

La base de datos contiene cuatro tablas principales:

| Tabla | Propósito | Información representativa |
|---|---|---|
| `cybershield_scenarios` | Escenarios ejecutados | Nombre, tipo, fechas y metadatos |
| `cybershield_processes` | Procesos ficticios | PID, nombre, estado, prioridad, CPU y RAM |
| `cybershield_events` | Historial de actividad | Tipo de evento, detalle, fecha y referencias |
| `cybershield_alerts` | Alertas de la simulación | Tipo, gravedad, descripción, fecha y proceso relacionado |

### Relaciones y llaves

- Cada tabla tiene una llave primaria `id` de tipo UUID.
- `owner_id` referencia al usuario de `auth.users` y permite asociar los registros con su propietario.
- `scenario_id` relaciona procesos, eventos y alertas con un escenario.
- `process_id`, presente en eventos y alertas, puede relacionarlos con un registro de proceso.
- `process_pid` conserva el identificador de proceso simulado como dato de referencia.

Las referencias anteriores corresponden a las restricciones declaradas en el archivo SQL. El PID es un identificador de la simulación; no es el identificador de un proceso real del sistema operativo.

### Seguridad y acceso a datos

- RLS está habilitado en las cuatro tablas.
- Las políticas limitan las operaciones a filas cuyo `owner_id` coincide con `auth.uid()`.
- Los permisos distinguen entre lectura, inserción y actualización según la tabla.
- El frontend utiliza una clave publicable y depende de la sesión de Supabase Auth para operar con los datos protegidos.

**Nota sobre persistencia:** el dashboard web recupera el escenario más reciente del usuario y los procesos, eventos y alertas vinculados a ese escenario. No debe interpretarse como una restauración automática de todos los escenarios históricos. La exportación JSON corresponde al registro de eventos disponible en la sesión de la interfaz.

## 🔐 Configuración de Supabase

El archivo `supabase/schema.sql` contiene la definición de tablas, relaciones, índices, permisos y políticas RLS.

Para preparar una instancia propia:

1. Crea un proyecto en Supabase.
2. Abre **SQL Editor** y ejecuta el esquema de `supabase/schema.sql`.
3. En **Authentication**, configura los métodos de acceso y las URL de redirección de acuerdo con el dominio donde publiques la aplicación.
4. Revisa que la URL y la clave publicable utilizadas por el frontend correspondan a tu proyecto.
5. Crea una cuenta de prueba y verifica el registro, inicio de sesión y aislamiento de datos entre usuarios.

> [!WARNING]
> Nunca publiques claves `service_role`, claves secretas, contraseñas ni archivos `.env`. La clave publicable está diseñada para clientes, pero no reemplaza la autenticación ni las políticas RLS.

## 🚀 Ejecutar y probar

### Aplicación web publicada

Abre directamente:

**https://jhonnatanlopez2006-alt.github.io/CyberShield/**

Para probarla:
1. Regístrate o inicia sesión.
2. Ejecuta el escenario normal.
3. Crea o selecciona un proceso y prueba sus acciones.
4. Ejecuta el escenario de actividad sospechosa.
5. Consulta las alertas y el registro de eventos.
6. Comprueba la persistencia desde Supabase con el mismo usuario.

### Prototipo de escritorio Python

El repositorio también conserva un prototipo académico de escritorio basado en Python y Tkinter, organizado en módulos dentro de `src/`. Para preparar ese entorno:

```bash
git clone https://github.com/jhonnatanlopez2006-alt/CyberShield.git
cd CyberShield
python -m pip install -r requirements.txt
```

La integración Python/Supabase dispone de documentación y código en `documentacion/integracion_supabase.md` e `integracion/`. La configuración de escritorio es independiente del despliegue web: sigue las instrucciones específicas de esa documentación antes de intentar conectar ese prototipo.

## 🗂️ Estructura del repositorio

```text
CyberShield/
├── documentacion/                 # Arquitectura, requisitos y guías
│   ├── diagramas/                 # Diagramas de funcionamiento
│   ├── arquitectura_inicial.md
│   ├── descripcion_proyecto.md
│   ├── integracion_supabase.md
│   ├── requerimientos.md
│   └── tecnologias.md
├── integracion/                   # Repositorio de persistencia Python/Supabase
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

## 🧪 Pruebas del prototipo Python

Para ejecutar las pruebas automatizadas:

```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```

## 📚 Documentación adicional

- [Arquitectura inicial](documentacion/arquitectura_inicial.md)
- [Descripción del proyecto](documentacion/descripcion_proyecto.md)
- [Integración con Supabase](documentacion/integracion_supabase.md)
- [Tecnologías](documentacion/tecnologias.md)
- [Requerimientos](documentacion/requerimientos.md)
- [Esquema de base de datos](supabase/schema.sql)

## ⚠️ Alcance y limitaciones

- La simulación utiliza métricas y procesos ficticios.
- Las reglas de alertas son didácticas y no equivalen a detección real de malware.
- La persistencia requiere conexión, sesión válida y políticas RLS configuradas en Supabase.
- La aplicación web publicada y el prototipo Python/Tkinter son componentes distintos dentro del mismo repositorio; sus mecanismos de inicio y configuración no deben confundirse.

## 📄 Licencia

Consulta el archivo [LICENSE](LICENSE) para conocer las condiciones de uso y distribución.

---

<p align="center">
  <strong>CyberShield · Laboratorio de procesos y seguridad informática</strong><br>
  Proyecto académico · Universidad Manuela Beltrán
</p>
