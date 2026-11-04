# Requerimientos

## Funcionales
| ID | Requerimiento |
|---|---|
| RF-01 | Crear procesos ficticios desde la aplicación. |
| RF-02 | Mostrar PID, nombre, estado, prioridad, CPU y memoria. |
| RF-03 | Pausar y reanudar procesos simulados. |
| RF-04 | Finalizar procesos simulados. |
| RF-05 | Alertar cuando CPU o memoria simuladas superen umbrales. |
| RF-06 | Identificar patrones simulados, como creación masiva de procesos. |
| RF-07 | Ejecutar escenarios predefinidos. |
| RF-08 | Registrar eventos y alertas en un historial local. |
| RF-09 | Presentar estadísticas y gráficas de recursos. |

## No funcionales
| ID | Requerimiento |
|---|---|
| RNF-01 | Interfaz clara y fácil de utilizar. |
| RNF-02 | Código modular y mantenible. |
| RNF-03 | Mensajes de alerta comprensibles. |
| RNF-04 | Compatibilidad prevista con Windows 10/11 y Linux. |
| RNF-05 | Resultados reproducibles con configuración y semilla equivalentes. |
| RNF-06 | No interactuar con procesos reales ni ejecutar código malicioso. |
| RNF-07 | Almacenar eventos en formato local legible, como JSON. |
| RNF-08 | Mantener documentación técnica y guía de ejecución. |

## Criterios iniciales de aceptación
- La aplicación inicia sin errores.
- Se visualiza al menos un proceso ficticio.
- Se reflejan los cambios de estado.
- Una métrica que supera un umbral genera una alerta.
- Los eventos pueden consultarse en el historial.
