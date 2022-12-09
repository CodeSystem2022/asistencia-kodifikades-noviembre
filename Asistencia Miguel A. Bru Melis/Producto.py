# Asistencia, Alumno: Miguel Angel Bru Melis.

class Producto:
    contador_productos = 0 # Varible que le pertenece a la clase, de esta forma podemos usarla como contador.

  # Constructor de Producto (init)
    def __init__(self, nombre, precio): 
        Producto.contador_productos += 1  # Hacemos uso de la variable de clase.
        self._id_producto = Producto.contador_productos # El id de cada producto es automático según el contador.
        self._nombre = nombre
        self._precio = precio

    # Método GET de precio
    @property
    def precio(self):
        return self._precio

   # Método SET de precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio
      
  # Método GET de nombre
    @property
    def nombre(self):
        return self._nombre

   # Método SET de nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

  # Método toString para imprimir los Productos.
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'