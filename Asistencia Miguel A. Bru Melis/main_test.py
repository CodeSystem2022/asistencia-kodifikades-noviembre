# Asistencia, Alumno: Miguel Angel Bru Melis.

# Necesitamos importar las clases Producto y Orden.
from Orden import Orden
from Producto import Producto

producto1 = Producto('Televisor', 30000.00)
producto2 = Producto('Licuadora', 10000.00)
producto3 = Producto('Aire Acondicionado', 25000.00)
producto4 = Producto('Celular', 20000.00)
producto5 = Producto('Aspiradora', 8500.00)
producto6 = Producto('Heladera', 35000.00)

# Generamos una orden (Orden 1)
productos1 = [producto4, producto5] # Lista de productos.
orden1 = Orden(productos1) # Creamos un objeto de tipo Orden enviado la lista productos.
orden1.incorporar_producto(producto2)
orden1.incorporar_producto(producto1)
print(orden1)
print(f'El total de la orden 1 es: {orden1.calcular_total()}')

# Generamos una orden (Orden 2)
productos2 = [producto1, producto3,producto6]
orden2 = Orden(productos2)
orden2.incorporar_producto(producto2)
orden2.incorporar_producto(producto4)
print(f'\n{orden2}')
print(f'El total de la orden 2 es: {orden2.calcular_total()}')

# Generamos una orden (Orden 3)
productos3 = [producto3, producto2]
orden3 = Orden(productos3)
orden3.incorporar_producto(producto4)
orden3.incorporar_producto(producto6)
print(f'\n{orden3}')
print(f'El total de la orden 3 es: {orden3.calcular_total()}')


print('\n Ejercicio realizado por Miguel Angel Bru Melis')

