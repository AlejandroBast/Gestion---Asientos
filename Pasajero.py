
class Pasajero:
#---------------------------------------------------------
## Clase pasajero y atributos
#---------------------------------------------------------
    def __init__(self, Cedula, Nombre):
        self.Cedula = Cedula
        self.Nombre = Nombre
        
#---------------------------------------------------------
## Metodos
#--------------------------------------------------------
    def darCedula(self):
        return self.Cedula
    
    def darNombre(self ): 
        return self.Nombre
