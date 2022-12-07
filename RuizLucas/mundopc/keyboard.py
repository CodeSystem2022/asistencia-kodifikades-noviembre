from input_device import InputDevice

class Keyboard(InputDevice):
  keyboardCount = 0

  def __init__(self, marca, input__type):
    Keyboard.keyboardCount += 1
    self._id_keyboard = Keyboard.keyboardCount
    super().__init__(marca,input__type)

  def __str__(self):
    return f'Id: {self._id_keyboard}, Marca: {self._marca}, Input type: {self._input__type}'

