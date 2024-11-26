from computadora import Computadora

class Celular(Computadora):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                 procesador, fuente_poder, almacenamiento, memoria_ram, sensor_huella,
                 nfc, camara, tipo_conexion):
        super().__init__(fabricante, fecha_fabricacion, marca, modelo, sistema_operativo,
                         procesador, fuente_poder, almacenamiento, memoria_ram)
        self._sensor_huella = sensor_huella
        self._nfc = nfc
        self._camara = camara
        self._tipo_conexion = tipo_conexion

    def get_sensor_huella(self):
        return self._sensor_huella

    def set_sensor_huella(self, sensor_huella):
        self._sensor_huella = sensor_huella

    def get_nfc(self):
        return self._nfc

    def set_nfc(self, nfc):
        self._nfc = nfc

    def get_camara(self):
        return self._camara

    def set_camara(self, camara):
        self._camara = camara

    def get_tipo_conexion(self):
        return self._tipo_conexion

    def set_tipo_conexion(self, tipo_conexion):
        self._tipo_conexion = tipo_conexion
