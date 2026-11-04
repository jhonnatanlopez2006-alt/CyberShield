# CyberShield
## Simulador de detección de amenazas y monitoreo de procesos

**Universidad:** Universidad Manuela Beltrán  
**Asignatura:** Sistemas Operativos  
**Integrantes:** Jhonnatan Alexander Lopez Muñoz y Juan Gabriel Gutierrez Trujillo

### Descripción
CyberShield es un proyecto académico que propone una aplicación de escritorio didáctica para simular la administración y supervisión de procesos. Permitirá visualizar procesos ficticios, consultar estados y consumo estimado de CPU y memoria, ejecutar escenarios controlados, detectar patrones sospechosos y registrar eventos.

> La demostración inicial usa datos ficticios. No inspecciona, modifica ni finaliza procesos reales del sistema y no ejecuta malware.

### Problemática
Los conceptos de procesos, planificación, concurrencia, gestión de recursos y seguridad pueden ser difíciles de comprender solo desde la teoría. CyberShield busca facilitar su aprendizaje mediante una representación visual y simulaciones controladas.

### Objetivo general
Desarrollar una aplicación didáctica que simule el monitoreo y la administración de procesos, identifique comportamientos sospechosos mediante reglas y registre eventos en un entorno seguro.

### Objetivos específicos
- Visualizar PID, nombre, estado, prioridad, CPU y memoria de procesos simulados.
- Simular creación, pausa, reanudación y finalización de procesos.
- Calcular y representar consumo ficticio de recursos.
- Detectar patrones anómalos con umbrales configurables.
- Ejecutar escenarios normales y sospechosos.
- Registrar alertas y resultados.

### Alcance
Esta primera entrega contiene la formulación, requerimientos, arquitectura, diagramas, estructura del código y una maqueta web estática para visualizar la propuesta. La implementación funcional se desarrollará por etapas.

### Funcionalidades previstas
1. Panel de procesos simulados.
2. Gestión del ciclo de vida simulado.
3. Monitoreo de CPU y memoria ficticias.
4. Detección de consumo elevado y creación masiva simulada.
5. Escenarios de demostración.
6. Historial de eventos y alertas.
7. Estadísticas y gráficas.

### Arquitectura
- Interfaz de usuario.
- Gestor de procesos.
- Detector de amenazas.
- Gestor de recursos.
- Registro de eventos.
- Gestor de escenarios.

### Tecnologías
Python 3.10+, Tkinter (interfaz de escritorio prevista), HTML/CSS/JavaScript (maqueta visual), Matplotlib (gráficas opcionales), JSON, Git y GitHub.

### Requisitos iniciales
- Windows 10/11 o Linux con entorno gráfico.
- Python 3.10 o superior.
- Navegador web moderno para abrir la maqueta.
- Git y Visual Studio Code recomendados.

### Ejecución de la maqueta
Abre `vista_web/index.html` en un navegador. No requiere instalación ni servidor.

### Ejecución del prototipo Python
Desde la raíz del proyecto:
```bash
python src/main.py
```
La interfaz de escritorio inicial usa Tkinter.

### Estructura
```text
CyberShield/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── documentacion/
├── vista_web/
├── src/
├── pruebas/
└── recursos/
```

### Estado
Planeación y estructuración inicial. La maqueta web es una representación visual de la propuesta, no el producto final conectado al simulador.

### Próximos avances
Completar la interfaz de escritorio, integrar los módulos de simulación, implementar reglas de detección, persistencia de eventos y pruebas.

### Referencias técnicas
- Python Software Foundation. (s. f.). *Python documentation*. https://docs.python.org/3/
- Python Software Foundation. (s. f.). *Tkinter documentation*. https://docs.python.org/3/library/tkinter.html
- Git. (s. f.). *Git documentation*. https://git-scm.com/doc
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
