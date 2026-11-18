# CyberShield

**Simulador didáctico de procesos y alertas de ciberseguridad**

**Asignatura:** Sistemas Operativos  
**Institución:** Universidad Manuela Beltrán  
**Autores:** Jhonnatan Alexander Lopez Muñoz y Juan Gabriel Gutierrez Trujillo

## Descripción
Prototipo académico en Python y Tkinter para estudiar gestión de procesos, estados, prioridades, consumo simulado de CPU y memoria, escenarios y alertas didácticas.

> **Alcance de seguridad:** los procesos y recursos son ficticios. CyberShield no inspecciona, modifica ni finaliza procesos reales del sistema operativo y no ejecuta malware.

## Requisitos
- Python 3.10 o superior.
- Windows 10/11 o Linux con Tkinter.
- Conexión a Internet para la persistencia en Supabase.

## Instalación
```bash
git clone https://github.com/jhonnatanlopez2006-alt/CyberShield.git
cd CyberShield
python -m pip install -r requirements.txt
python src/main.py
```

## Funcionalidades
- Crear, iniciar, pausar, reanudar y finalizar procesos simulados.
- Consultar CPU y RAM ficticias.
- Ejecutar escenarios normales y sospechosos.
- Generar alertas didácticas y registrar eventos.
- Persistencia local JSONL y capa de integración Supabase preparada.

## Configuración de Supabase
Consulta [documentacion/integracion_supabase.md](documentacion/integracion_supabase.md) y ejecuta [supabase/schema.sql](supabase/schema.sql) en el SQL Editor del proyecto CyberShield. Completa `.env.example` en un archivo local `.env`; nunca subas este último a GitHub.

La base usa RLS y requiere una sesión autenticada. El dashboard web estático todavía no incorpora login ni se debe conectar con claves privilegiadas.

## Pruebas
```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```

## Estructura
```text
CyberShield/
├── documentacion/
├── integracion/
├── pruebas/
├── recursos/imagenes/
├── src/
├── supabase/schema.sql
├── .env.example
├── index.html
└── requirements.txt
```

## Limitaciones
CyberShield es un simulador didáctico. Las métricas no reflejan uso real del equipo ni constituyen detección real de malware. La persistencia Supabase requiere aplicar el esquema y configurar autenticación.
