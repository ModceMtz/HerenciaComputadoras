class Origen:
    def __init__(self, fabricante, fecha_fabricacion):
        self.fabricante = fabricante
        self.fecha_fabricacion = fecha_fabricacion

    def mostrar_fecha_fabricacion(self):
        return f"Fabricante: {self.fabricante}, Fecha de fabricación: {self.fecha_fabricacion}"