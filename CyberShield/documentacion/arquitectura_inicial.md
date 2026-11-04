# Arquitectura inicial

## Estilo
Arquitectura modular: la interfaz presenta información y solicita operaciones a los módulos especializados.

## Componentes
| Componente | Responsabilidad | Tecnología |
|---|---|---|
| Interfaz | Mostrar procesos, alertas y controles | Python / Tkinter |
| Gestor de procesos | Crear y cambiar estados ficticios | Python |
| Detector de amenazas | Evaluar reglas de anomalía | Python |
| Gestor de recursos | Calcular métricas simuladas | Python |
| Registro de eventos | Guardar historial | JSON |
| Escenarios | Configurar simulaciones | Python |

## Flujo
1. El usuario selecciona un escenario.
2. El gestor de escenarios crea acciones simuladas.
3. El gestor de procesos actualiza los estados.
4. El gestor de recursos calcula métricas ficticias.
5. El detector evalúa umbrales y patrones.
6. El registro guarda eventos.
7. La interfaz actualiza tablas e indicadores.

## Límite de seguridad
Los procesos son objetos internos del programa. No se consultan, modifican ni terminan procesos reales del sistema.
