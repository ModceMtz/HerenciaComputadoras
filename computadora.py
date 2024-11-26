from origen import Origen

class Computadora(Origen):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                 procesador, fuente_poder, almacenamiento, memoria_ram):
        super().__init__(fabricante, fecha_fabricacion)
        self._marca = marca
        self._modelo = modelo
        self._sistema_operativo = sistema_operativo
        self._procesador = procesador
        self._fuente_poder = fuente_poder
        self._almacenamiento = almacenamiento
        self._memoria_ram = memoria_ram

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_sistema_operativo(self):
        return self._sistema_operativo

    def set_sistema_operativo(self, sistema_operativo):
        self._sistema_operativo = sistema_operativo

    def get_procesador(self):
        return self._procesador

    def set_procesador(self, procesador):
        self._procesador = procesador

    def get_fuente_poder(self):
        return self._fuente_poder

    def set_fuente_poder(self, fuente_poder):
        self._fuente_poder = fuente_poder

    def get_almacenamiento(self):
        return self._almacenamiento

    def set_almacenamiento(self, almacenamiento):
        self._almacenamiento = almacenamiento

    def get_memoria_ram(self):
        return self._memoria_ram

    def set_memoria_ram(self, memoria_ram):
        self._memoria_ram = memoria_ram
