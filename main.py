class Motor:
    def __init__(self, numeroCilindros:int, tipo:str, registro:int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    # @property
    # def getterMotor(self):
    #     return self.numeroCilindros, self.tipo, self.registro
    
    def cambiarRegistro(self, new_registro:int):
        self.registro = new_registro

    def asignarTipo(self, new_tipo):
        tipos_posibles_de_cambio = ("electrico", "gasolina")
        for i in tipos_posibles_de_cambio:
            if new_tipo == i:
                self.tipo = new_tipo

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo:str, precio:int, asientos, marca, motor, registro:int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
            numAsientos = 0
            for asiento in self.asientos:
                if asiento is not None:
                    numAsientos += 1
            return numAsientos
        
    def verificarIntegridad(self):
            if self.registro == self.motor.registro:
                for asiento in self.asientos:
                    if asiento is not None:
                        if asiento.registro != self.registro:
                            return "Las piezas no son originales"
                return "Auto original"
            else:
                return "Las piezas no son originales"

class Asiento:
    def __init__(self, color:str, precio:int, registro:int):
        self.color = color
        self.precio = precio
        self.registro = registro

    # @property
    # def getterAsiento(self):
    #     return self.color, self.precio, self.registro

    def cambiarColor(self, new_color):
        lista_colores_posibles = ["rojo", "amarillo", "verde", "negro", "blanco"]
        for i in lista_colores_posibles:
            if new_color == i:
                 self.color = new_color
