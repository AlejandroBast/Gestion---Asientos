from Pasajero import Pasajero
from Clase import Clase
from Ubicacion import Ubicacion

class Silla:

    def __init__(self, pNumero, pClase, pUbicacion):
        self.__numero = pNumero
        self.__clase = pClase
        self.__ubicacion = pUbicacion
        # estado del asiento
        self.__pasajero = None
        
    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    def desAsignarSilla(self):
        self.__pasajero = None

    def sillaAsignada(self):
        return self.__pasajero is not None

    def darNumero(self):
        return self.__numero

    def darClase(self):
        return self.__clase

    def darUbicacion(self):
        return self.__ubicacion
    
    def darPasajeroOcupante(self):
        if self.__pasajero is not None:
            print(self.__pasajero.darNombre())
        else:
            print("No hay pasajero asignado a esta silla.")