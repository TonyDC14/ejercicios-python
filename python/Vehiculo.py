from enum import Enum
from abc import ABC

class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
        PINK = 4
        BLACK = 5
        WHITE = 6
        ORANGE = 7
        YELLOW = 8

class TipoBicicleta(Enum):
        URBANA = 1
        DEPORTIVA = 2

class Vehiculo(ABC):
    def __init__(self, color, ruedas):
        self.color : Color = color
        self.ruedas = ruedas

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo : TipoBicicleta = tipo

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad_kmh, cilindrada_cc):
        super().__init__(color, ruedas, tipo)
        self.velocidad_kmh = velocidad_kmh
        self.cilindrada_cc = cilindrada_cc

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad_kmh, cilindrada_cc):
        super().__init__(color, ruedas)
        self.velocidad_kmh = velocidad_kmh
        self.cilindrada_cc = cilindrada_cc

class Camioneta(Coche):
   
    def __init__(self, color, ruedas, velocidad_kmh, cilindrada_cc, carga):
        super().__init__(color, ruedas, velocidad_kmh, cilindrada_cc)
        self.carga = carga

vehiculos = [
    Bicicleta(Color.RED, 2, TipoBicicleta.URBANA),
    Bicicleta(Color.YELLOW, 2, TipoBicicleta.URBANA),
    Motocicleta(Color.BLACK, 2, TipoBicicleta.DEPORTIVA, 200, 125),
    Motocicleta(Color.RED, 2, TipoBicicleta.DEPORTIVA, 170, 125),
    Coche(Color.ORANGE, 4, 210, 3000),
    Coche(Color.BLACK, 4, 170, 500),
    Camioneta(Color.WHITE, 4, 140, 3000, 600),
    Camioneta(Color.BLUE, 4, 150, 500, 2300)
]

def catalogar(listaVehiculos, ruedas = -1):

    listaVehiculosFiltrados = []

    if ruedas != -1:
        # Removemos de la lista aquellos vehiculos qu no coincidan
        for vehiculo in listaVehiculos:
            if vehiculo.ruedas == ruedas:
                listaVehiculosFiltrados.append(vehiculo)
    else:
        listaVehiculosFiltrados = listaVehiculos

    contador = 0
    for vehiculo in listaVehiculosFiltrados:
        contador+=1
        print("nombre de la clase : " + vehiculo.__class__.__name__)
        print("atributos : " + str(vehiculo.__dict__))
        print("----------------------------------------------------------------------------")

    if ruedas != -1:
        print("Se han encontrado {" + str(contador) + "} vehículos con {" + str(ruedas) + "} ruedas")

#catalogar(vehiculos, 4)
#catalogar(vehiculos, 2)
#catalogar(vehiculos, 0)
catalogar(vehiculos)

