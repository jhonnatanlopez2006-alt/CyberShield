# Fase II - Desarrollo e implementación

## Alcance implementado
CyberShield pasa de una propuesta documental a un prototipo de escritorio en Python y Tkinter. Todo el monitoreo es ficticio; no se consultan ni manipulan procesos reales.

## Componentes
- `src/procesos/gestor_procesos.py`: procesos con PID incremental, nombre, estado, prioridad, CPU y memoria; transiciones validadas.
- `src/recursos/gestor_recursos.py`: agregación de métricas simuladas.
- `src/seguridad/detector_amenazas.py`: alertas por CPU >= 80%, memoria >= 1024 MB y nombre sospechoso.
- `src/escenarios/simulador_escenarios.py`: escenarios reproducibles normal y sospechoso.
- `src/eventos/registro_eventos.py`: eventos JSONL en `registros/eventos.jsonl`.
- `src/interfaz/ventana_principal.py`: interfaz gráfica con tabla, controles y alertas.
- `pruebas/test_simulador.py`: pruebas unitarias de componentes.

## Configuración del entorno
Windows 10/11 o Linux con entorno gráfico, Python 3.10+ y Tkinter disponible. No se requieren paquetes de terceros para el prototipo. En algunas distribuciones Linux, Tkinter se instala por separado.

## Ejecución
Desde la raíz del repositorio:
```bash
python src/main.py
```
En Windows, también puede utilizarse `py src/main.py`.

## Pruebas
```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```
Estas pruebas no requieren interfaz gráfica.

## Demostración sugerida
1. Abrir la interfaz y cargar «Escenario normal»; comprobar ausencia de alertas.
2. Seleccionar un proceso, iniciar, pausar y reanudar; observar los estados.
3. Cargar «Escenario sospechoso»; observar alertas por CPU, memoria y nombre.
4. Consultar `registros/eventos.jsonl` para comprobar la persistencia.
5. Ejecutar las pruebas unitarias y registrar el resultado.

## Evidencias
El código, las pruebas y los commits son evidencia verificable de implementación. Las capturas de pantalla de la interfaz y la ejecución en un equipo Windows/Linux deben obtenerse después de ejecutar el prototipo localmente; no se incluyen capturas fabricadas.

## Limitaciones
Las métricas no representan el consumo real del sistema; la suma de CPU se limita visualmente a 100%. No hay planificación real, concurrencia ni detección de malware. Los procesos finalizados permanecen visibles para fines didácticos.
