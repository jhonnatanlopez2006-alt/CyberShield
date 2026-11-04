# 🛡️ CyberShield
## Simulador de detección de amenazas y monitoreo de procesos

**Universidad:** Universidad Manuela Beltrán  
**Asignatura:** Sistemas Operativos  
**Integrantes:** Jhonnatan Alexander Lopez Muñoz y Juan Gabriel Gutierrez Trujillo

## Descripción general
CyberShield es una propuesta de aplicación didáctica para simular la administración y supervisión de procesos de un sistema operativo. Permitirá visualizar procesos ficticios, consultar sus estados y consumo estimado de CPU y memoria, ejecutar escenarios controlados, identificar comportamientos sospechosos y registrar eventos.

> **Entorno seguro:** los procesos, métricas y alertas son simulados. El proyecto no inspecciona, modifica ni finaliza procesos reales del equipo y no ejecuta malware.

## Problemática
Los conceptos de procesos, planificación, concurrencia, gestión de recursos y seguridad pueden ser difíciles de comprender únicamente desde la teoría. CyberShield propone una herramienta visual para experimentar con esos conceptos sin poner en riesgo el equipo.

## Objetivo general
Desarrollar una aplicación didáctica que simule el monitoreo y la administración de procesos, detecte comportamientos sospechosos mediante reglas y registre eventos en un entorno controlado.

## Objetivos específicos
- Visualizar PID, nombre, estado, prioridad y consumo simulado de CPU y memoria.
- Simular creación, pausa, reanudación y finalización de procesos.
- Detectar consumo elevado y patrones anómalos ficticios.
- Ejecutar escenarios normales y sospechosos.
- Registrar alertas y consultar estadísticas de la simulación.

## Alcance inicial
Esta primera entrega establece la formulación, los requerimientos, la arquitectura y la organización inicial del código. La implementación se desarrollará por etapas durante el semestre.

## Funcionalidades previstas
1. Panel de procesos simulados.
2. Gestión del ciclo de vida de los procesos.
3. Monitoreo de CPU y memoria ficticias.
4. Detección de anomalías con umbrales configurables.
5. Ejecución de escenarios de simulación.
6. Historial de eventos y alertas.
7. Estadísticas y gráficas.

## Arquitectura propuesta
| Componente | Responsabilidad |
|---|---|
| Interfaz de usuario | Mostrar procesos, alertas y controles |
| Gestor de procesos | Crear y administrar procesos simulados |
| Detector de amenazas | Evaluar reglas e identificar anomalías |
| Gestor de recursos | Calcular consumo ficticio de CPU y memoria |
| Registro de eventos | Guardar el historial local |
| Gestor de escenarios | Preparar simulaciones normales y sospechosas |

## Tecnologías previstas
- Python 3.10 o superior.
- Tkinter para la interfaz de escritorio inicial.
- HTML5, CSS3 y JavaScript para la maqueta web.
- JSON para registros locales.
- Matplotlib (opcional) para gráficas.
- Git y GitHub para control de versiones.
- Visual Studio Code como entorno de desarrollo.

## Requisitos iniciales
- Windows 10/11 o Linux con entorno gráfico.
- Python 3.10+ para el prototipo de escritorio.
- Navegador moderno para abrir la maqueta web.

## Estructura del repositorio
```text
CyberShield/
├── README.md
├── index.html
├── styles.css
├── app.js
├── documentacion/
├── src/
├── pruebas/
├── recursos/
└── vista_web/
```

## Ejecutar la maqueta web
Abre `index.html` en el navegador o visita el sitio publicado mediante GitHub Pages cuando finalice la publicación.

## Estado del proyecto
**Fase 1 – Planeación y estructuración inicial.** La maqueta web es una representación visual con datos ficticios; todavía no está conectada a la lógica Python.

## Próximos avances
- Implementar la interfaz de escritorio.
- Desarrollar el gestor de procesos simulados.
- Integrar el detector de amenazas y el gestor de recursos.
- Incorporar persistencia de eventos.
- Ejecutar pruebas y documentar resultados.

## Referencias técnicas
- Python Software Foundation. (s. f.). *Python documentation*. https://docs.python.org/3/
- Python Software Foundation. (s. f.). *Tkinter documentation*. https://docs.python.org/3/library/tkinter.html
- Git. (s. f.). *Git documentation*. https://git-scm.com/doc
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.

---
**CyberShield – Proyecto académico de Sistemas Operativos | Universidad Manuela Beltrán.**
