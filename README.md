# CyberShield - Fase II

**Simulador didáctico de procesos y alertas de ciberseguridad**

**Universidad:** Universidad Manuela Beltrán  
**Asignatura:** Sistemas Operativos  
**Integrantes:** Jhonnatan Alexander Lopez Muñoz y Juan Gabriel Gutierrez Trujillo

## Descripción
Aplicación de escritorio en Python/Tkinter para estudiar procesos ficticios, sus estados, prioridades, métricas simuladas de CPU y memoria, escenarios normales/sospechosos y alertas. **No inspecciona ni modifica procesos reales, ni ejecuta malware.**

## Requisitos
- Python 3.10 o superior.
- Windows 10/11 o Linux con entorno gráfico.
- Tkinter (incluido habitualmente en Python para Windows; en algunas distribuciones Linux debe instalarse por separado).
- No se necesitan dependencias externas para esta versión.

## Ejecutar
Desde la raíz del repositorio:
```bash
python src/main.py
```
En Windows también: `py src/main.py`.

## Pruebas automatizadas
```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```

## Funciones implementadas
1. Crear procesos simulados con PID, nombre, prioridad y recursos.
2. Iniciar, pausar, reanudar y finalizar procesos ficticios con validación de estados.
3. Visualizar tabla de procesos y totales de CPU y memoria simuladas.
4. Cargar escenarios reproducibles «Normal» y «Sospechoso».
5. Detectar consumo elevado y patrones ficticios sospechosos.
6. Registrar acciones y alertas en `registros/eventos.jsonl`.
7. Ejecutar pruebas unitarias sin interfaz gráfica.

## Estructura
- `src/main.py`: inicio de la aplicación.
- `src/interfaz/`: ventana Tkinter.
- `src/procesos/`: modelo y gestor de procesos.
- `src/recursos/`: métricas simuladas.
- `src/seguridad/`: detector didáctico.
- `src/escenarios/`: escenarios de prueba.
- `src/eventos/`: registro JSONL.
- `pruebas/`: pruebas unitarias.
- `documentacion/fase_ii.md`: arquitectura, ejecución y evidencias de Fase II.

## Demostración
Ejecutar la aplicación, cargar «Escenario normal», administrar estados de procesos y luego cargar «Escenario sospechoso» para observar las alertas. Consultar el registro JSONL y ejecutar las pruebas unitarias.

**Evidencias pendientes de obtener localmente:** capturas reales de la interfaz y salida de pruebas en Windows/Linux. No se afirma que exista una validación visual hasta ejecutarla.

## Documentación
La propuesta de la Fase I permanece en `documentacion/`. Consultar [documentación técnica de Fase II](documentacion/fase_ii.md).

## Límites
Los procesos y recursos son enteramente simulados; no hay intervención sobre el sistema operativo anfitrión.
