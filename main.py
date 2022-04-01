import sys
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtGui
from ui_main import Ui_MainWindow
from classes.client import Cliente
from control.clientControl import ClienteControl

class ShowApp(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None) -> None:
    super().__init__(parent)
    super().setupUi(self)
    self.initComponents()
    self.ClienteControl = ClienteControl()
    self.cor_sucesso = "background-color:rgb(209,255,209);"
    self.cor_erro = "background-color: rgb(250, 185, 185);"
    
  def listarClientes(self):
    contLinhas = 0
    self.tbWCliente.setRowCount(10)
    for cliente in self.ClienteControl.listaClientes:
      self.tbWCliente.setItem(0, 0, QtGui.QtWidgets.QTableWidgetItem(cliente.nome))
      self.tbWCliente.setItem(contLinhas, 1, QtGui.QtWidgets.QTableWidgetItem(cliente.cpf))
      self.tbWCliente.setItem(contLinhas, 2, QtGui.QtWidgets.QTableWidgetItem(cliente.email))
      self.tbWCliente.setItem(contLinhas, 3, QtGui.QtWidgets.QTableWidgetItem(cliente.endereco))
      self.tbWCliente.setItem(contLinhas, 4, QtGui.QtWidgets.QTableWidgetItem(cliente.fone))
      self.tbWCliente.setItem(contLinhas, 5, QtGui.QtWidgets.QTableWidgetItem(cliente.bairro))
      self.tbWCliente.setItem(contLinhas, 6, QtGui.QtWidgets.QTableWidgetItem(cliente.categoria))
      contLinhas += 1
    
  def salvarClientes(self):
    cliente = Cliente()
    cliente.nome = self.txtNomeCli.text()
    cliente.cpf = self.txtCpfCli.text()
    cliente.email = self.txtEmailCli.text()
    cliente.endereco = self.txtEndCli.text()
    cliente.fone = self.txtFoneCli.text()
    cliente.bairro = self.txtBairroCli.text()
    cliente.categoria = self.cboCategCli.currentText()
    
    if len(cliente.erro_validacao) != 0:
      self.lblMsg.setText(cliente.erro_validacao)
      self.frameMsg.show()
      self.lblMsg.setStyleSheet(self.cor_erro)
    else:
      msg = self.ClienteControl.salvarCliente(cliente)
      self.lblMsg.setText(msg)
      self.frameMsg.show()
      self.lblMsg.setStyleSheet(self.cor_sucesso)
      self.listarClientes()
      
  def initComponents(self):
    img = QImage('files/img/logo1.png')
    self.label_2.setPixmap(QPixmap.fromImage(img))
    self.btnCliente.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageClientes))
    self.btnProduto.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageProdutos))
    self.btnSalvarCli.clicked.connect(self.salvarClientes)
    self.frameMsg.hide()
    self.btnExcluirMsg.clicked.connect(lambda: self.frameMsg.hide())
    
if __name__ == '__main__':
  qt = QApplication(sys.argv)
  view = ShowApp()
  view.show()
  qt.exec()