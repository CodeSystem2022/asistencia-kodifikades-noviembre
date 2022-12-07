class Monitor:
  monitorCount = 0

  def __init__(self, marca, size):
    Monitor.monitorCount += 1
    self._id_monitor = Monitor.monitorCount
    self._marca = marca
    self._size = size

  def __str__(self):
    return f'Id: {self._id_monitor}, Marca: {self._marca}, Size: {self._size}'
