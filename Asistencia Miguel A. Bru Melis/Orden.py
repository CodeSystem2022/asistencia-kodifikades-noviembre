# Asistencia, Alumno: Miguel Angel Bru Melis.

from Producto import Producto # Necesitamos importar los productos para crear la orden.

class Orden:
    contador_orden = 0 # Varible que le pertenece a la clase, de esta forma podemos usarla como contador.

  # Constructor de Orden (init)
    def __init__(self, lista_productos):
        Orden.contador_orden += 1  # Hacemos uso de la variable de clase.
        self._id_orden = Orden.contador_orden  # El id de cada orden es automático según el contador.
        self._lista_productos = list(lista_productos) # Para crear una orden debemos suministrar una lista de productos.

  # Método para añadir productos
    def incorporar_producto(self, producto):
        self._lista_productos.append(producto) 

  # Método para calcular el total
    def calcular_total(self):
        cuenta_total = 0  # Variable del método que va sumando el valor por cada producto.
        for producto in self._lista_productos:
            cuenta_total += producto.precio
        return cuenta_total

    # Método toString para imprimir la orden.
    def __str__(self):
        lista_productos_str = '' # Variable donde se añadirán cadenas (productos) en el bucle for. 
        for producto in self._lista_productos:
            lista_productos_str += producto.__str__() + ' - '  # usamos el método toString de producto.
        return f'Orden: {self._id_orden}, \nProducto: {lista_productos_str}' # Retornamos la nueva cadena generada luego del bucle for.

