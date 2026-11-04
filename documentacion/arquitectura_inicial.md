# Arquitectura inicial

## Estilo arquitectónico
Se propone una arquitectura modular por responsabilidades. La interfaz será el punto de interacción con el usuario y se comunicará con módulos especializados.

## Componentes
| Componente | Responsabilidad | Tecnología prevista |
|---|---|---|
| Interfaz de usuario | Presentar información, alertas y controles | Python / Tkinter o PyQt5 |
| Gestor de procesos | Administrar procesos simulados y sus estados | Python |
| Detector de amenazas | Evaluar reglas y reconocer patrones simulados | Python |
| Gestor de recursos | Calcular uso ficticio de CPU y memoria | Python |
| Registro de eventos | Almacenar eventos y alertas | JSON / TXT |
| Gestor de escenarios | Configurar simulaciones didácticas | Python |

## Diagrama de arquitectura
```mermaid
flowchart TB
  U[Estudiante] --> UI[Interfaz de usuario]
  UI --> ES[Gestor de escenarios]
  ES --> GP[Gestor de procesos]
  GP --> GR[Gestor de recursos]
  GR --> DT[Detector de amenazas]
  DT --> RE[Registro de eventos]
  RE --> UI
  GR --> UI
```

## Diagrama de funcionamiento
```mermaid
flowchart LR
  A[Usuario] --> B[Configura escenario]
  B --> C[Simulación de procesos]
  C --> D[Estimación de CPU y memoria]
  D --> E[Evaluación de reglas]
  E --> F{¿Se detecta anomalía?}
  F -- Sí --> G[Generar alerta simulada]
  F -- No --> H[Continuar simulación]
  G --> I[Registrar evento]
  H --> I
  I --> J[Actualizar información]
```

## Ciclo de vida de proceso simulado
```mermaid
stateDiagram-v2
  [*] --> Nuevo
  Nuevo --> Listo
  Listo --> Ejecucion
  Ejecucion --> Bloqueado
  Bloqueado --> Listo
  Ejecucion --> Terminado
  Terminado --> [*]
```

## Restricción de seguridad
Los procesos serán objetos internos de la simulación. El proyecto no leerá, modificará ni finalizará procesos reales del sistema operativo, ni ejecutará amenazas reales.