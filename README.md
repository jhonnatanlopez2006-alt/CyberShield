# CyberShield

**Simulador didáctico de procesos y alertas de ciberseguridad**

**Asignatura:** Sistemas Operativos  
**Institución:** Universidad Manuela Beltrán  
**Autores:** Jhonnatan Alexander Lopez Muñoz y Juan Gabriel Gutierrez Trujillo

## Descripción
CyberShield es un prototipo de escritorio desarrollado en Python y Tkinter para estudiar la gestión de procesos, estados, prioridades, consumo simulado de CPU y memoria, escenarios de comportamiento y generación de alertas didácticas.

> **Alcance de seguridad:** los procesos y recursos son ficticios. La aplicación no inspecciona, modifica ni finaliza procesos reales del sistema operativo y no ejecuta malware.

## Requisitos
- Python 3.10 o superior.
- Windows 10/11 o Linux con entorno gráfico.
- Tkinter disponible. En algunas distribuciones Linux debe instalarse por separado.
- No se requieren dependencias externas para el prototipo actual.

## Instalación y ejecución
Clona el repositorio y entra a la carpeta:

```bash
git clone https://github.com/jhonnatanlopez2006-alt/CyberShield.git
cd CyberShield
python src/main.py
```

En Windows también puedes usar `py src/main.py`.

## Funcionalidades
- Crear y administrar procesos simulados con PID, nombre y prioridad.
- Iniciar, pausar, reanudar y finalizar procesos respetando transiciones de estado.
- Consultar una tabla de procesos y métricas ficticias de CPU y memoria.
- Cargar escenarios «Normal» y «Sospechoso».
- Generar alertas didácticas por umbrales de consumo y nombres sospechosos.
- Registrar eventos en formato JSONL.
- Ejecutar pruebas unitarias de los componentes.

## Ejecutar pruebas
Desde la raíz del proyecto:

```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```

Las pruebas automatizadas no necesitan abrir la interfaz gráfica. Registra la salida real de este comando al realizar la validación local; no se asume que las pruebas hayan sido ejecutadas solo por estar incluidas en el repositorio.

## Estructura del proyecto

```text
CyberShield/
├── documentacion/       # Arquitectura, requerimientos y desarrollo
├── pruebas/             # Pruebas unitarias
├── recursos/imagenes/   # Recursos visuales
├── src/
│   ├── interfaz/        # Interfaz Tkinter
│   ├── procesos/        # Gestión de procesos simulados
│   ├── recursos/        # Métricas ficticias
│   ├── seguridad/       # Reglas de detección didáctica
│   ├── escenarios/      # Escenarios de simulación
│   ├── eventos/         # Registro de eventos
│   └── main.py          # Punto de entrada
├── index.html           # Dashboard web demostrativo
└── requirements.txt
```

## Recorrido de demostración
1. Inicia la aplicación con el comando indicado.
2. Carga el escenario normal y revisa los procesos y sus métricas.
3. Prueba los controles de estado de un proceso.
4. Carga el escenario sospechoso y observa las alertas.
5. Consulta el registro de eventos generado y ejecuta las pruebas unitarias.

## Documentación
- [Descripción del proyecto](documentacion/descripcion_proyecto.md)
- [Arquitectura inicial](documentacion/arquitectura_inicial.md)
- [Tecnologías](documentacion/tecnologias.md)
- [Desarrollo de Fase II](documentacion/fase_ii.md)
- [Pruebas](pruebas/README.md)

## Evidencias de entrega
Añade en `evidencias/` capturas reales de: ventana principal, escenario normal, escenario sospechoso/alertas y salida de las pruebas unitarias. Estas evidencias requieren ejecutar el proyecto en un equipo local; no se incluyen imágenes simuladas ni resultados no verificados.

## Limitaciones conocidas
CyberShield es una herramienta académica de simulación. Las métricas no representan el uso real del equipo; no implementa planificación real del sistema operativo, concurrencia ni detección de malware real.
