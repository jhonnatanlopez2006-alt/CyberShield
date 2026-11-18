# Pruebas automatizadas

El archivo `test_simulador.py` contiene pruebas unitarias de los componentes de simulación.

## Ejecución
Desde la raíz del repositorio:

```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```

En Windows también puede utilizarse:

```powershell
py -m unittest discover -s pruebas -p "test_*.py" -v
```

## Alcance
Las pruebas cubren la creación y transición de estados de procesos, la validación de transiciones no permitidas, el cálculo de recursos simulados, la carga de escenarios y detección de alertas, y la persistencia del registro.

## Evidencia del resultado
Guarda la salida real de la consola en la carpeta de evidencias de la entrega. La existencia de los casos de prueba no implica que hayan sido ejecutados en todos los sistemas operativos.
