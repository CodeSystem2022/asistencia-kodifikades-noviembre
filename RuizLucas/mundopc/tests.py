from mouse import Mouse
from keyboard import Keyboard
from monitor import Monitor
from computer import Computer
from order import Order


keyboard = Keyboard('HP', 'USB')
monitor = Monitor('Lenovo', '32 pulgadas')
mouse = Mouse('Lenovo', 'Bluethoot')
computer1 = Computer('ASUS', monitor, keyboard, mouse)

keyboard2 = Keyboard('ASUS', 'USB')
monitor2 = Monitor('ASUS', '32 pulgadas')
mouse2 = Mouse('ASUS', 'Bluethoot')
computer2 = Computer('ASUS', monitor, keyboard, mouse)

computers = [computer1, computer2]
order = Order(computers)
print(order)