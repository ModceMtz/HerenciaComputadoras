from ComputadoraEscritorio import ComputadoraDeEscritorio

class ComputadoraMini(ComputadoraDeEscritorio):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                 procesador, fuente_poder, almacenamiento, memoria_ram, gabinete,
                 sistema_refrigeracion, tamano, teclado, mouse, pantalla):
        super().__init__(fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                         procesador, fuente_poder, almacenamiento, memoria_ram, gabinete,
                         sistema_refrigeracion, teclado, mouse, pantalla)
        self._tamano = tamano

    def get_tamano(self):
        return self._tamano

    def set_tamano(self, tamano):
        self._tamano = tamano
