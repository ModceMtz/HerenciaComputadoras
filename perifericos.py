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
