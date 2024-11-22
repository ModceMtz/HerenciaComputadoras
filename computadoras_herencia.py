class Origen:
    def __init__(self, fabricante, fecha_fabricacion):
        self.fabricante = fabricante
        self.fecha_fabricacion = fecha_fabricacion

    def mostrar_fecha_fabricacion(self):
        return f"Fabricante: {self.fabricante}, Fecha de fabricación: {self.fecha_fabricacion}"


class Computadoras(Origen):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram):
        super().__init__(fabricante, fecha_fabricacion)
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.procesador = procesador
        self.bateria_fuente = bateria_fuente
        self.almacenamiento = almacenamiento
        self.memoria_ram = memoria_ram

    def encender(self):
        return f"{self.marca} {self.modelo} está encendida."

    def apagar(self):
        return f"{self.marca} {self.modelo} está apagada."

    def actualizar_sistema_operativo(self, nuevo_sistema):
        self.sistema_operativo = nuevo_sistema
        return f"Sistema operativo actualizado a {nuevo_sistema}."


class Laptops(Computadoras):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram, peso, teclado_integrado, tipo):
        super().__init__(fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram)
        self.peso = peso
        self.teclado_integrado = teclado_integrado
        self.tipo = tipo

    def abrir(self):
        return "La laptop está abierta."

    def cerrar(self):
        return "La laptop está cerrada."


class Celular(Computadoras):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram, sensor_huella, nfc, camara, tipo_conexion):
        super().__init__(fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram)
        self.sensor_huella = sensor_huella
        self.nfc = nfc
        self.camara = camara
        self.tipo_conexion = tipo_conexion

    def desbloquear_con_huella(self):
        return "Celular desbloqueado con huella."

    def usar_nfc(self):
        return "NFC activado."


class ComputadorasDeEscritorio(Computadoras):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram, gabinete, sistema_refrigeracion):
        super().__init__(fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram)
        self.gabinete = gabinete
        self.sistema_refrigeracion = sistema_refrigeracion

    def configurar_pantalla(self, configuracion):
        return f"Pantalla configurada a: {configuracion}."

    def conectar_mouse_teclado(self, mouse, teclado):
        return f"Mouse ({mouse}) y teclado ({teclado}) conectados."


class ComputadoraMini(ComputadorasDeEscritorio):
    def __init__(self, fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram, gabinete, sistema_refrigeracion, tamaño):
        super().__init__(fabricante, fecha_fabricacion, marca, modelo, sistema_operativo, procesador, bateria_fuente, almacenamiento, memoria_ram, gabinete, sistema_refrigeracion)
        self.tamaño = tamaño

    def mostrar_tamaño(self):
        return f"Esta computadora mini tiene un tamaño de {self.tamaño}."


laptop = Laptops(
    "HP", "2023-05-10", "HP", "Pavilion", "Windows 11",
    "Intel Core i7", "Batería de 6 celdas", "1TB", "16GB",
    "1.5kg", "Alfanumérico con retroiluminación", "Gamer"
)

celular = Celular(
    "Samsung", "2023-03-01", "Samsung", "Galaxy S23", "Android 13",
    "Exynos 2200", "4000mAh", "256GB", "12GB",
    "Sensor ultrasónico", "Sí", {"Cámaras": 3, "Pixeles": [108, 12, 10]}, "5G"
)

escritorio = ComputadorasDeEscritorio(
    "Dell", "2022-12-15", "Dell", "OptiPlex", "Windows 10",
    "Intel Core i5", "Fuente de 500W", "512GB", "8GB",
    "ATX", "Refrigeración líquida"
)

mini = ComputadoraMini(
    "Lenovo", "2023-01-20", "Lenovo", "ThinkCentre", "Linux",
    "AMD Ryzen 5", "Fuente de 250W", "256GB", "8GB",
    "Mini-ITX", "Refrigeración pasiva", "20x20x5 cm"
)

print(laptop.abrir())
print(celular.desbloquear_con_huella())
print(escritorio.conectar_mouse_teclado("Logitech", "Corsair"))
print(mini.mostrar_tamaño())
