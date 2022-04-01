class Cliente:
  def __init__(self, nome=None, cpf=None, email=None, endereco=None, fone=None, bairro=None, categoria=None):
    self.nome = nome
    self.cpf = cpf
    self.email = email
    self.endereco = endereco
    self.fone = fone
    self.bairro = bairro
    self.categoria = categoria
    self.erro_validacao = ""
    
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome):
    if nome != None and len(nome) != 0:
      self.__nome = nome
    else:
      self.erro_validacao = f"O Campo [NOME] é obrigatório!"
  
  @property
  def cpf(self):
    return self.__cpf
  
  @cpf.setter
  def cpf(self, cpf):
    self.__cpf = cpf
    
  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, email):
    self.__email = email
    
  @property
  def endereco(self):
    return self.__endereco
  
  @endereco.setter
  def endereco(self, endereco):
    self.__endereco = endereco
    
  @property
  def fone(self):
    return self.__fone
  
  @fone.setter
  def fone(self, fone):
    self.__fone = fone
  
  @property
  def bairro(self):
    return self.__bairro
  
  @bairro.setter
  def bairro(self, bairro):
    self.__bairro = bairro
  
  @property
  def categoria(self):
    return self.__categoria
  
  @categoria.setter
  def categoria(self, categoria):
    self.__categoria = categoria
    