# CyberShield
## Simulador de detección de amenazas y monitoreo de procesos

**Universidad:** Universidad Manuela Beltrán  
**Asignatura:** Sistemas Operativos  
**Integrantes:**
- Jhonnatan Alexander Lopez Muñoz
- Juan Gabriel Gutierrez Trujillo

---

## 1. Descripción general
CyberShield es una propuesta de aplicación didáctica que permitirá simular la administración y supervisión de procesos de un sistema operativo. El producto se plantea para visualizar procesos simulados, analizar su estado y consumo estimado de CPU y memoria, reconocer comportamientos sospechosos y registrar eventos en un entorno controlado.

## 2. Problemática
Los conceptos de procesos, planificación, concurrencia, gestión de recursos y seguridad pueden ser difíciles de comprender únicamente desde la teoría. Se plantea una herramienta didáctica que permita observar y explorar esos conceptos mediante simulaciones.

## 3. Justificación
CyberShield busca relacionar los contenidos de Sistemas Operativos con una propuesta práctica y organizada. El entorno simulado permitirá estudiar estados de procesos y métricas de recursos sin afectar el computador del usuario.

## 4. Objetivo general
Desarrollar una aplicación de escritorio didáctica que simule el monitoreo y la administración de procesos, permita analizar recursos, detectar comportamientos sospechosos y registrar eventos en un entorno controlado.

## 5. Objetivos específicos
- Representar procesos simulados con PID, nombre, estado y prioridad.
- Proponer operaciones de creación, pausa, reanudación y finalización de procesos ficticios.
- Estimar y mostrar el uso de CPU y memoria dentro de la simulación.
- Definir reglas para detectar patrones sospechosos simulados.
- Plantear escenarios de prueba y un registro de eventos y alertas.

## 6. Alcance inicial
Esta primera entrega corresponde a la fase de planeación y estructuración. Incluye la descripción del producto, levantamiento de información, requerimientos, arquitectura inicial, tecnologías previstas y organización del repositorio. La implementación funcional se realizará en fases posteriores.

**Límite de seguridad:** la propuesta trabajará con procesos y métricas simuladas. No inspeccionará, modificará ni finalizará procesos reales del equipo y no ejecutará malware.

## 7. Usuarios o beneficiarios
Estudiantes y docentes interesados en comprender conceptos de administración de procesos, planificación, memoria, CPU, concurrencia y monitoreo.

## 8. Funcionalidades principales previstas
1. Visualizar PID, nombre, estado, prioridad y métricas simuladas.
2. Crear y administrar procesos ficticios.
3. Representar el ciclo de vida de los procesos.
4. Calcular consumo simulado de CPU y memoria.
5. Aplicar reglas de detección de comportamientos anómalos ficticios.
6. Definir escenarios normales y sospechosos.
7. Registrar eventos y alertas.

## 9. Arquitectura y estructura general
El producto se organizará en seis módulos: interfaz de usuario, gestor de procesos, detector de amenazas, gestor de recursos, registro de eventos y gestor de escenarios.

La estructura detallada se encuentra en `documentacion/estructura_producto.md` y la arquitectura en `documentacion/arquitectura_inicial.md`.

## 10. Tecnologías previstas
- Python 3.10 o superior.
- Tkinter o PyQt5 para la futura interfaz de escritorio (selección por confirmar).
- Bibliotecas estándar de Python para la lógica de simulación.
- JSON o TXT para registros locales.
- Matplotlib como opción para gráficas.
- Git y GitHub para control de versiones.
- Visual Studio Code como entorno de desarrollo.

## 11. Requisitos iniciales de hardware y software
**Hardware recomendado:** computador de doble núcleo o superior, 4 GB de RAM o más y espacio disponible para el proyecto.

**Software previsto:** Windows 10/11 o Linux con entorno gráfico; Python 3.10 o superior; Git y un editor de código.

## 12. Relación con Sistemas Operativos
El proyecto se relaciona con procesos, PID, estados y ciclo de vida, planificación, prioridades, hilos y concurrencia, gestión de CPU y memoria, administración de recursos y conceptos básicos de monitoreo y seguridad.

## 13. Estado actual y próximos avances
**Estado actual:** primera entrega de planeación, documentación y estructura inicial. No se presenta todavía una aplicación funcional.

**Próximos avances:** definir el framework gráfico, diseñar los modelos de procesos, implementar los módulos, integrar escenarios, realizar pruebas y documentar resultados.

## 14. Organización de la documentación
- `documentacion/descripcion_proyecto.md`
- `documentacion/levantamiento_informacion.md`
- `documentacion/requerimientos.md`
- `documentacion/arquitectura_inicial.md`
- `documentacion/tecnologias.md`
- `documentacion/estructura_producto.md`
- `documentacion/referencias.md`
- `documentacion/diagramas/`

## 15. Referencias
Consultar `documentacion/referencias.md` para las fuentes técnicas y bibliográficas.

---
**CyberShield — Proyecto académico de Sistemas Operativos | Universidad Manuela Beltrán.**