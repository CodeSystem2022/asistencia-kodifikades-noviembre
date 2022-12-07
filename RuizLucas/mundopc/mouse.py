from input_device import InputDevice

class Mouse(InputDevice):
  mouseCount = 0

  def __init__(self, marca, input__type):
    Mouse.mouseCount += 1
    self._id_mouse = Mouse.mouseCount
    super().__init__(marca,input__type)

  def __str__(self):
    return f'Id: {self._id_mouse}, Marca: {self._marca}, Input type: {self._input__type}'
