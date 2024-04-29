from Pasajero import Pasajero
from Silla import Silla
from Ubicacion import Ubicacion
from Clase import Clase

# instanciar el pasajero
pasajero1 = Pasajero(354868, "Juan Perez")

# instanciar la clase
economica = Clase("Economica")
ejecutiva = Clase("Ejecutiva")

# instanciar la ubicacion
ventana = Ubicacion("Ventana")
centro = Ubicacion("Centro")
pasillo = Ubicacion("Pasillo")

# instanciar la silla
asiento1 = Silla(32, economica, ventana)
asiento1.asignarPasajero(pasajero1)
asiento1.darPasajeroOcupante()
asiento1.desAsignarSilla()
asiento1.darPasajeroOcupante()

