from laptop import Laptop
from celular import Celular
from ComputadoraEscritorio import ComputadoraDeEscritorio
from computadora_mini import ComputadoraMini

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
