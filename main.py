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

    def __init__(self, modelo:str, precio:int, marca:str, registro:int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = []
        self.marca = marca
        self.registro = registro

    # @property
    # def getterAsientos

    def cantidadAsientos(self, color, precio, registro):
        nuevo_asiento = Asiento(color, precio, registro)
        self.asientos.append(nuevo_asiento)
        print(len(self.asientos))

    def verificarIntegridad(self, ObjetoAsiento, ObjetoMotor, ObjetoAuto):
        if ObjetoAsiento.registro == ObjetoAuto.registro == ObjetoMotor.registro:
            print("Auto Original")
        else:
            print("Las piezas no son originales")


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
