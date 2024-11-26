class Origen:
    def __init__(self, fabricante, fecha_fabricacion):
        self._fabricante = fabricante
        self._fecha_fabricacion = fecha_fabricacion

    # Getters y Setters
    def get_fabricante(self):
        return self._fabricante

    def set_fabricante(self, fabricante):
        self._fabricante = fabricante

    def get_fecha_fabricacion(self):
        return self._fecha_fabricacion

    def set_fecha_fabricacion(self, fecha_fabricacion):
        self._fecha_fabricacion = fecha_fabricacion
