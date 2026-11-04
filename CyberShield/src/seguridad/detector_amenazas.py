class DetectorAmenazas:
    """Evalúa métricas ficticias con umbrales didácticos."""
    def __init__(self, umbral_cpu=85.0, umbral_memoria_mb=500):
        self.umbral_cpu = umbral_cpu
        self.umbral_memoria_mb = umbral_memoria_mb

    def analizar(self, proceso):
        alertas = []
        if proceso.cpu >= self.umbral_cpu:
            alertas.append(f"CPU elevada en {proceso.nombre}")
        if proceso.memoria_mb >= self.umbral_memoria_mb:
            alertas.append(f"Memoria elevada en {proceso.nombre}")
        return alertas
