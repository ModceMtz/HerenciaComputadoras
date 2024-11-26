class Origen:
    def __init__(self, fabricante, fecha_fabricacion):
        self._fabricante = fabricante
        self._fecha_fabricacion = fecha_fabricacion

    def get_fabricante(self):
        return self._fabricante

    def set_fabricante(self, fabricante):
        self._fabricante = fabricante

    def get_fecha_fabricacion(self):
        return self._fecha_fabricacion

    def set_fecha_fabricacion(self, fecha_fabricacion):
        self._fecha_fabricacion = fecha_fabricacion


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


class Perifericos:
    def __init__(self, teclado, mouse, pantalla):
        self._teclado = teclado
        self._mouse = mouse
        self._pantalla = pantalla

    def get_teclado(self):
        return self._teclado

    def set_teclado(self, teclado):
        self._teclado = teclado

    def get_mouse(self):
        return self._mouse

    def set_mouse(self, mouse):
        self._mouse = mouse

    def get_pantalla(self):
        return self._pantalla

    def set_pantalla(self, pantalla):
        self._pantalla = pantalla


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


if __name__ == "__main__":

    laptop = Laptop(
        fabricante="Dell", fecha_fabricacion="2023-01-15", marca="Dell Inspiron", modelo="15 3000",
        sistema_operativo="Windows 11", procesador="Intel Core i5", fuente_poder="Batería 42Wh",
        almacenamiento="512GB SSD", memoria_ram="8GB", peso="1.8kg",
        teclado_integrado="Teclado retroiluminado QWERTY", tipo="Ultrabook"
    )
    print("### Laptop ###")
    print(f"Fabricante: {laptop.get_fabricante()}")
    print(f"Fecha de fabricación: {laptop.get_fecha_fabricacion()}")
    print(f"Marca: {laptop.get_marca()}")
    print(f"Modelo: {laptop.get_modelo()}")
    print(f"Sistema operativo: {laptop.get_sistema_operativo()}")
    print(f"Procesador: {laptop.get_procesador()}")
    print(f"Fuente de poder: {laptop.get_fuente_poder()}")
    print(f"Almacenamiento: {laptop.get_almacenamiento()}")
    print(f"Memoria RAM: {laptop.get_memoria_ram()}")
    print(f"Peso: {laptop.get_peso()}")
    print(f"Teclado integrado: {laptop.get_teclado_integrado()}")
    print(f"Tipo: {laptop.get_tipo()}")
    print()

    celular = Celular(
        fabricante="Samsung", fecha_fabricacion="2023-06-10", marca="Galaxy S22", modelo="Ultra",
        sistema_operativo="Android 13", procesador="Exynos 2200", fuente_poder="Batería 5000mAh",
        almacenamiento="1TB", memoria_ram="12GB", sensor_huella=True, nfc=True,
        camara={"Principal": "108MP", "Ultra Wide": "12MP"}, tipo_conexion="5G"
    )
    print("### Celular ###")
    print(f"Fabricante: {celular.get_fabricante()}")
    print(f"Fecha de fabricación: {celular.get_fecha_fabricacion()}")
    print(f"Marca: {celular.get_marca()}")
    print(f"Modelo: {celular.get_modelo()}")
    print(f"Sistema operativo: {celular.get_sistema_operativo()}")
    print(f"Procesador: {celular.get_procesador()}")
    print(f"Fuente de poder: {celular.get_fuente_poder()}")
    print(f"Almacenamiento: {celular.get_almacenamiento()}")
    print(f"Memoria RAM: {celular.get_memoria_ram()}")
    print(f"Sensor de huella: {celular.get_sensor_huella()}")
    print(f"NFC: {celular.get_nfc()}")
    print(f"Cámara: {celular.get_camara()}")
    print(f"Tipo de conexión: {celular.get_tipo_conexion()}")
    print()

    escritorio = ComputadoraDeEscritorio(
        fabricante="HP", fecha_fabricacion="2022-11-30", marca="Pavilion", modelo="Desktop TP01",
        sistema_operativo="Windows 10", procesador="Intel Core i7", fuente_poder="600W PSU",
        almacenamiento="1TB HDD", memoria_ram="16GB", gabinete="ATX", sistema_refrigeracion="Aire",
        teclado="Mecánico", mouse="Óptico", pantalla="27 pulgadas"
    )
    print("### Computadora de Escritorio ###")
    print(f"Fabricante: {escritorio.get_fabricante()}")
    print(f"Fecha de fabricación: {escritorio.get_fecha_fabricacion()}")
    print(f"Marca: {escritorio.get_marca()}")
    print(f"Modelo: {escritorio.get_modelo()}")
    print(f"Sistema operativo: {escritorio.get_sistema_operativo()}")
    print(f"Procesador: {escritorio.get_procesador()}")
    print(f"Fuente de poder: {escritorio.get_fuente_poder()}")
    print(f"Almacenamiento: {escritorio.get_almacenamiento()}")
    print(f"Memoria RAM: {escritorio.get_memoria_ram()}")
    print(f"Gabinete: {escritorio.get_gabinete()}")
    print(f"Sistema de refrigeración: {escritorio.get_sistema_refrigeracion()}")
    print(f"Teclado: {escritorio.get_teclado()}")
    print(f"Mouse: {escritorio.get_mouse()}")
    print(f"Pantalla: {escritorio.get_pantalla()}")
    print()

    mini = ComputadoraMini(
        fabricante="Apple", fecha_fabricacion="2023-05-15", marca="Mac Mini", modelo="M2",
        sistema_operativo="macOS Ventura", procesador="Apple M2", fuente_poder="Interna",
        almacenamiento="256GB SSD", memoria_ram="8GB", gabinete="Mini", sistema_refrigeracion="Pasiva",
        tamano="19.7 x 19.7 x 3.6 cm", teclado="Inalámbrico", mouse="Magic Mouse", pantalla="No incluida"
    )
    print("### Computadora Mini ###")
    print(f"Fabricante: {mini.get_fabricante()}")
    print(f"Fecha de fabricación: {mini.get_fecha_fabricacion()}")
    print(f"Marca: {mini.get_marca()}")
    print(f"Modelo: {mini.get_modelo()}")
    print(f"Sistema operativo: {mini.get_sistema_operativo()}")
    print(f"Procesador: {mini.get_procesador()}")
    print(f"Fuente de poder: {mini.get_fuente_poder()}")
    print(f"Almacenamiento: {mini.get_almacenamiento()}")
    print(f"Memoria RAM: {mini.get_memoria_ram()}")
    print(f"Gabinete: {mini.get_gabinete()}")
    print(f"Sistema de refrigeración: {mini.get_sistema_refrigeracion()}")
    print(f"Tamaño: {mini.get_tamano()}")
    print(f"Teclado: {mini.get_teclado()}")
    print(f"Mouse: {mini.get_mouse()}")
    print(f"Pantalla: {mini.get_pantalla()}")
    print()
