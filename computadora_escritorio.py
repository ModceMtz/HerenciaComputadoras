from computadora import Computadora
from perifericos import Perifericos

class ComputadoraDeEscritorio(Computadora, Perifericos):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                 procesador, fuente_poder, almacenamiento, memoria_ram, gabinete,
                 sistema_refrigeracion, teclado, mouse, pantalla):
        Computadora.__init__(self, fabricante, fecha_fabricacion, marca, modelo,
                             sistema_operativo, procesador, fuente_poder, almacenamiento, memoria_ram)
        Perifericos.__init__(self, teclado, mouse, pantalla)
        self._gabinete = gabinete
        self._sistema_refrigeracion = sistema_refrigeracion

    def get_gabinete(self):
        return self._gabinete

    def set_gabinete(self, gabinete):
        self._gabinete = gabinete

    def get_sistema_refrigeracion(self):
        return self._sistema_refrigeracion

    def set_sistema_refrigeracion(self, sistema_refrigeracion):
        self._sistema_refrigeracion = sistema_refrigeracion
