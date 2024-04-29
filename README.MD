# Gestión de Asientos de Avión

Este proyecto consiste en un sistema de gestión de asientos de avión, desarrollado en Python. El sistema permite asignar y desasignar pasajeros a asientos de diferentes clases y ubicaciones en un avión.

## Estructura del Proyecto

El proyecto está organizado en varios archivos que contienen las clases necesarias para el funcionamiento del sistema:

- `Pasajero.py`: Contiene la definición de la clase `Pasajero`, que representa a un pasajero y gestiona su información personal.
- `Clase.py`: Define la clase `Clase`, que representa el tipo de clase de un asiento de avión, como "Económica" o "Ejecutiva".
- `Ubicacion.py`: Define la clase `Ubicacion`, que representa la ubicación de un asiento de avión, como "Ventana", "Centro" o "Pasillo".
- `Silla.py`: Contiene la definición de la clase `Silla`, que representa un asiento de avión y gestiona la asignación de pasajeros a ese asiento.

## Uso del Sistema

Para utilizar el sistema de gestión de asientos de avión, se deben seguir los siguientes pasos:

1. Importar las clases necesarias desde los archivos correspondientes.
2. Instanciar objetos de las clases `Pasajero`, `Clase` y `Ubicacion` según sea necesario.
3. Crear instancias de la clase `Silla`, especificando el número de asiento, la clase y la ubicación.
4. Asignar un pasajero a una silla utilizando el método `asignarPasajero`.
5. Verificar si una silla está ocupada utilizando el método `sillaAsignada`.
6. Obtener información sobre una silla, como su número, clase, ubicación y el pasajero asignado, utilizando los métodos correspondientes.

El sistema proporciona una interfaz sencilla para la gestión de asientos de avión, lo que facilita la asignación y desasignación de pasajeros de manera eficiente.

## Ejemplo de Uso

A continuación se muestra un ejemplo de cómo utilizar el sistema de gestión de asientos de avión:

```python
from Pasajero import Pasajero
from Silla import Silla
from Ubicacion import Ubicacion
from Clase import Clase

# Instanciar el pasajero
pasajero1 = Pasajero(354868, "Juan Perez")

# Instanciar la clase
economica = Clase("Economica")
ejecutiva = Clase("Ejecutiva")

# Instanciar la ubicacion
ventana = Ubicacion("Ventana")
centro = Ubicacion("Centro")
pasillo = Ubicacion("Pasillo")

# Instanciar la silla
asiento1 = Silla(32, economica, ventana)
asiento1.asignarPasajero(pasajero1)
asiento1.darPasajeroOcupante()
asiento1.desAsignarSilla()
asiento1.darPasajeroOcupante()
```

En este ejemplo, se crea un pasajero, se definen clases y ubicaciones, se crea una silla y se asigna el pasajero a esa silla. Luego se imprime el nombre del pasajero asignado a la silla, se desasigna la silla y se muestra un mensaje indicando que no hay pasajero asignado.