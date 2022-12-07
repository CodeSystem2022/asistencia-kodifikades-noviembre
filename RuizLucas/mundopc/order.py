class Order:
  orderCount = 0

  def __init__(self, computers):
    Order.orderCount += 1
    self._id_order = Order.orderCount
    self._computers = computers

  def addComputers(self, computers):
    self._computers.append(computers)

  def __str__(self):
    computers_str = ''
    for computers in self._computers:
      computers_str += computers.__str__()
      return f'''
        Order: {self._id_order},
        Computers: {computers_str}
      '''