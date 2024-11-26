from computadora import Computadora

class Laptop(Computadora):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                 procesador, fuente_poder, almacenamiento, memoria_ram, peso,
                 teclado_integrado, tipo):
        super().__init__(fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                         procesador, fuente_poder, almacenamiento, memoria_ram)
        self._peso = peso
        self._teclado_integrado = teclado_integrado
        self._tipo = tipo

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso

    def get_teclado_integrado(self):
        return self._teclado_integrado

    def set_teclado_integrado(self, teclado_integrado):
        self._teclado_integrado = teclado_integrado

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo
