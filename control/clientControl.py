from classes.client import Cliente

class ClienteControl:
  def __init__(self) -> None:
    self.listaClientes = None
    
  def salvarCliente(self, cliente):
    self.listaClientes.append(cliente)
    return "Cliente cadastrado com sucesso!"
  
  @property
  def listaClientes(self):
    return self.__listaClientes
  
  @listaClientes.setter
  def listaClientes(self, listaClientes):
    self.__listaClientes = []