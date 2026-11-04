# Arquitectura inicial

Se propone una arquitectura modular con seis componentes:

| Componente | Responsabilidad |
|---|---|
| Interfaz de usuario | Presentar datos, alertas y controles. |
| Gestor de procesos | Crear y administrar procesos simulados. |
| Detector de amenazas | Analizar reglas y detectar anomalías. |
| Gestor de recursos | Calcular consumo simulado de CPU y memoria. |
| Registro de eventos | Guardar el historial local. |
| Gestor de escenarios | Preparar simulaciones normales y sospechosas. |

## Flujo
Usuario → Interfaz → Escenario → Procesos → Recursos → Detector → Registro → Interfaz.

**Límite de seguridad:** la aplicación no consulta ni modifica procesos reales del sistema.
