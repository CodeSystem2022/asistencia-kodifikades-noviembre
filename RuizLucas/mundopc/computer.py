from keyboard import Keyboard
from monitor import Monitor
from mouse import Mouse

class Computer:
  computerCount = 0

  def __init__(self, name, monitor, keyboard, mouse):
    Computer.computerCount += 1
    self._id_computer = Computer.computerCount
    self._name = name
    self._monitor = monitor
    self._keyboard = keyboard
    self._mouse = mouse

  def __str__(self):
    return f'{self._name}: {self._id_computer}, Keyboard: {self._keyboard}, Monitor: {self._monitor}, Mouse: {self._mouse}'

