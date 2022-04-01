# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.8);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 100))
        self.label_2.setStyleSheet(u"color: #fff;")
        self.label_2.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.3);")
        self.mCadastros = QWidget()
        self.mCadastros.setObjectName(u"mCadastros")
        self.mCadastros.setGeometry(QRect(0, 0, 180, 344))
        self.verticalLayout_2 = QVBoxLayout(self.mCadastros)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnCliente = QPushButton(self.mCadastros)
        self.btnCliente.setObjectName(u"btnCliente")
        self.btnCliente.setMinimumSize(QSize(100, 50))
        self.btnCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCliente.setStyleSheet(u"QPushButton{\n"
"	background-color: #4CAF50;\n"
"  	border: none;\n"
"  	color: #fff;\n"
"  	padding: 16px 32px;\n"
"  	text-align: center;\n"
"  	text-decoration: none;\n"
"  	font-size: 16px;\n"
"  	margin: 4px 2px;\n"
"  	transition-duration: 0.4s;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"  	color: #4CAF50;\n"
"	font: 300 16px \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_2.addWidget(self.btnCliente)

        self.btnProduto = QPushButton(self.mCadastros)
        self.btnProduto.setObjectName(u"btnProduto")
        self.btnProduto.setMinimumSize(QSize(100, 50))
        self.btnProduto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnProduto.setStyleSheet(u"QPushButton{\n"
"	background-color: #4CAF50;\n"
"  	border: none;\n"
"  	color: #fff;\n"
"  	padding: 16px 32px;\n"
"  	text-align: center;\n"
"  	text-decoration: none;\n"
"  	font-size: 16px;\n"
"  	margin: 4px 2px;\n"
"  	transition-duration: 0.4s;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"  	color: #4CAF50;\n"
"	font: 300 16px \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_2.addWidget(self.btnProduto)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.mCadastros, u"Cadastros")
        self.mVendas = QWidget()
        self.mVendas.setObjectName(u"mVendas")
        self.mVendas.setGeometry(QRect(0, 0, 180, 344))
        self.toolBox.addItem(self.mVendas, u"Vendas")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frameMsg = QFrame(self.frame_3)
        self.frameMsg.setObjectName(u"frameMsg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frameMsg.sizePolicy().hasHeightForWidth())
        self.frameMsg.setSizePolicy(sizePolicy2)
        self.frameMsg.setFrameShape(QFrame.StyledPanel)
        self.frameMsg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameMsg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.lblMsg = QLabel(self.frameMsg)
        self.lblMsg.setObjectName(u"lblMsg")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lblMsg.sizePolicy().hasHeightForWidth())
        self.lblMsg.setSizePolicy(sizePolicy3)
        self.lblMsg.setMinimumSize(QSize(0, 25))
        self.lblMsg.setStyleSheet(u"background-color: #2196F3;\n"
"color: white;\n"
"opacity: 0.83;\n"
"transition: opacity 0.6s;")
        self.lblMsg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lblMsg)

        self.btnExcluirMsg = QPushButton(self.frameMsg)
        self.btnExcluirMsg.setObjectName(u"btnExcluirMsg")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnExcluirMsg.sizePolicy().hasHeightForWidth())
        self.btnExcluirMsg.setSizePolicy(sizePolicy4)
        self.btnExcluirMsg.setMinimumSize(QSize(5, 0))
        self.btnExcluirMsg.setMaximumSize(QSize(25, 16777215))
        self.btnExcluirMsg.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.btnExcluirMsg)


        self.verticalLayout_6.addWidget(self.frameMsg)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.1);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.Pages = QStackedWidget(self.frame_4)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.1);")
        self.pageShow = QWidget()
        self.pageShow.setObjectName(u"pageShow")
        self.verticalLayout_20 = QVBoxLayout(self.pageShow)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_11 = QFrame(self.pageShow)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_11)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_18.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_18.addWidget(self.label_9)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)


        self.verticalLayout_20.addWidget(self.frame_11)

        self.Pages.addWidget(self.pageShow)
        self.pageClientes = QWidget()
        self.pageClientes.setObjectName(u"pageClientes")
        self.verticalLayout_15 = QVBoxLayout(self.pageClientes)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabWidget_2 = QTabWidget(self.pageClientes)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.tabCli = QWidget()
        self.tabCli.setObjectName(u"tabCli")
        self.verticalLayout_12 = QVBoxLayout(self.tabCli)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_8 = QFrame(self.tabCli)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)
        self.label_6.setStyleSheet(u"padding: 10px;\n"
"background-color: #fff;\n"
"color: #000;\n"
"font-weight: 300;")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)

        self.txtNomeCli = QLineEdit(self.frame_8)
        self.txtNomeCli.setObjectName(u"txtNomeCli")
        self.txtNomeCli.setMinimumSize(QSize(0, 25))
        self.txtNomeCli.setStyleSheet(u"width: 100%;\n"
"padding: 5px 20px;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.txtNomeCli.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txtNomeCli, 2, 0, 1, 1)

        self.txtCpfCli = QLineEdit(self.frame_8)
        self.txtCpfCli.setObjectName(u"txtCpfCli")
        self.txtCpfCli.setMinimumSize(QSize(0, 25))
        self.txtCpfCli.setStyleSheet(u"width: 100%;\n"
"padding: 5px 20px;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.txtCpfCli.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txtCpfCli, 2, 1, 1, 1)

        self.txtEmailCli = QLineEdit(self.frame_8)
        self.txtEmailCli.setObjectName(u"txtEmailCli")
        self.txtEmailCli.setMinimumSize(QSize(0, 25))
        self.txtEmailCli.setStyleSheet(u"width: 100%;\n"
"padding: 5px 20px;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.txtEmailCli.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txtEmailCli, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy5)
        self.label_7.setStyleSheet(u"padding: 8px;\n"
"background-color: #2196F3;\n"
"color: white;\n"
"opacity: 0.83;\n"
"transition: opacity 0.6s;")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 2)

        self.txtEndCli = QLineEdit(self.frame_8)
        self.txtEndCli.setObjectName(u"txtEndCli")
        self.txtEndCli.setMinimumSize(QSize(0, 25))
        self.txtEndCli.setStyleSheet(u"width: 100%;\n"
"padding: 5px 20px;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.txtEndCli.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txtEndCli, 3, 1, 1, 1)

        self.txtFoneCli = QLineEdit(self.frame_8)
        self.txtFoneCli.setObjectName(u"txtFoneCli")
        self.txtFoneCli.setMinimumSize(QSize(0, 25))
        self.txtFoneCli.setStyleSheet(u"width: 100%;\n"
"padding: 5px 20px;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.txtFoneCli.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txtFoneCli, 4, 0, 1, 1)

        self.txtBairroCli = QLineEdit(self.frame_8)
        self.txtBairroCli.setObjectName(u"txtBairroCli")
        self.txtBairroCli.setMinimumSize(QSize(0, 25))
        self.txtBairroCli.setStyleSheet(u"width: 100%;\n"
"padding: 5px 20px;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.txtBairroCli.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txtBairroCli, 4, 1, 1, 1)

        self.cboCategCli = QComboBox(self.frame_8)
        self.cboCategCli.addItem("")
        self.cboCategCli.addItem("")
        self.cboCategCli.addItem("")
        self.cboCategCli.addItem("")
        self.cboCategCli.setObjectName(u"cboCategCli")
        self.cboCategCli.setStyleSheet(u"width: 100%;\n"
"padding: 5px 10px;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cboCategCli, 5, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.tabCli)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy5.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy5)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.btnSalvarCli = QPushButton(self.frame_9)
        self.btnSalvarCli.setObjectName(u"btnSalvarCli")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btnSalvarCli.sizePolicy().hasHeightForWidth())
        self.btnSalvarCli.setSizePolicy(sizePolicy6)
        self.btnSalvarCli.setMinimumSize(QSize(150, 30))
        self.btnSalvarCli.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSalvarCli.setLayoutDirection(Qt.RightToLeft)
        self.btnSalvarCli.setStyleSheet(u"QPushButton{\n"
"	background-color: #4CAF50;\n"
"  	border: none;\n"
"  	color: #fff;\n"
"  	padding: 16px 32px;\n"
"  	text-align: center;\n"
"  	text-decoration: none;\n"
"  	font-size: 16px;\n"
"  	margin: 4px 2px;\n"
"  	transition-duration: 0.4s;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"  	color: #4CAF50;\n"
"	font: 300 16px \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_14.addWidget(self.btnSalvarCli)


        self.verticalLayout_13.addWidget(self.frame_9)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)

        self.tabWidget_2.addTab(self.tabCli, "")
        self.tabCliList = QWidget()
        self.tabCliList.setObjectName(u"tabCliList")
        self.verticalLayout_16 = QVBoxLayout(self.tabCliList)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tbWCliente = QTableWidget(self.tabCliList)
        if (self.tbWCliente.columnCount() < 7):
            self.tbWCliente.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbWCliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbWCliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbWCliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbWCliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbWCliente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbWCliente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbWCliente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tbWCliente.setObjectName(u"tbWCliente")

        self.horizontalLayout_2.addWidget(self.tbWCliente)

        self.frame_10 = QFrame(self.tabCliList)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy7)
        self.frame_10.setMinimumSize(QSize(100, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btnAlterar = QPushButton(self.frame_10)
        self.btnAlterar.setObjectName(u"btnAlterar")
        self.btnAlterar.setMinimumSize(QSize(50, 50))
        self.btnAlterar.setStyleSheet(u"QPushButton{\n"
"	background-color: #4CAF50;\n"
"  	border: none;\n"
"  	color: #fff;\n"
"  	text-align: center;\n"
"  	text-decoration: none;\n"
"  	font-size: 14px;\n"
"  	transition-duration: 0.4s;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"  	color: #4CAF50;\n"
"	font: 300 14px \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_17.addWidget(self.btnAlterar)

        self.btnExcluir = QPushButton(self.frame_10)
        self.btnExcluir.setObjectName(u"btnExcluir")
        self.btnExcluir.setMinimumSize(QSize(50, 50))
        self.btnExcluir.setStyleSheet(u"QPushButton{\n"
"	background-color: #4CAF50;\n"
"  	border: none;\n"
"  	color: #fff;\n"
"  	padding: 16px 32px;\n"
"  	text-align: center;\n"
"  	text-decoration: none;\n"
"  	font-size: 16px;\n"
"  	margin: 4px 2px;\n"
"  	transition-duration: 0.4s;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"  	color: #4CAF50;\n"
"	font: 300 16px \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_17.addWidget(self.btnExcluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout_16.addLayout(self.horizontalLayout_2)

        self.tabWidget_2.addTab(self.tabCliList, "")

        self.verticalLayout_15.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pageClientes)
        self.pageProdutos = QWidget()
        self.pageProdutos.setObjectName(u"pageProdutos")
        self.verticalLayout_5 = QVBoxLayout(self.pageProdutos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.pageProdutos)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.tabProd = QWidget()
        self.tabProd.setObjectName(u"tabProd")
        self.verticalLayout_10 = QVBoxLayout(self.tabProd)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_6 = QFrame(self.tabProd)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setStyleSheet(u"padding: 10px;\n"
"background-color: #fff;\n"
"color: #000;\n"
"font-weight: 300;")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 25))
        self.lineEdit_3.setStyleSheet(u"width: 100%;\n"
"padding: 12px 20px;\n"
"margin: 8px 0;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setStyleSheet(u"width: 100%;\n"
"padding: 12px 20px;\n"
"margin: 8px 0;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 25))
        self.lineEdit_2.setStyleSheet(u"width: 100%;\n"
"padding: 12px 20px;\n"
"margin: 8px 0;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 25))
        self.lineEdit_4.setStyleSheet(u"width: 100%;\n"
"padding: 12px 20px;\n"
"margin: 8px 0;\n"
"display: inline-block;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)
        self.label_5.setStyleSheet(u"padding: 8px;\n"
"background-color: #2196F3;\n"
"color: white;\n"
"opacity: 0.83;\n"
"transition: opacity 0.6s;")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.tabProd)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btnSalvarProd = QPushButton(self.frame_7)
        self.btnSalvarProd.setObjectName(u"btnSalvarProd")
        sizePolicy6.setHeightForWidth(self.btnSalvarProd.sizePolicy().hasHeightForWidth())
        self.btnSalvarProd.setSizePolicy(sizePolicy6)
        self.btnSalvarProd.setMinimumSize(QSize(150, 30))
        self.btnSalvarProd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSalvarProd.setLayoutDirection(Qt.RightToLeft)
        self.btnSalvarProd.setStyleSheet(u"QPushButton{\n"
"	background-color: #4CAF50;\n"
"  	border: none;\n"
"  	color: #fff;\n"
"  	padding: 16px 32px;\n"
"  	text-align: center;\n"
"  	text-decoration: none;\n"
"  	font-size: 16px;\n"
"  	margin: 4px 2px;\n"
"  	transition-duration: 0.4s;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"  	color: #4CAF50;\n"
"	font: 300 16px \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_9.addWidget(self.btnSalvarProd)


        self.verticalLayout_8.addWidget(self.frame_7)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tabProd, "")
        self.tabProdList = QWidget()
        self.tabProdList.setObjectName(u"tabProdList")
        self.tabWidget.addTab(self.tabProdList, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pageProdutos)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.Pages.addWidget(self.page_4)

        self.verticalLayout_11.addWidget(self.Pages)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setStyleSheet(u"padding: 8px;\n"
"background-color: #2196F3;\n"
"color: white;\n"
"opacity: 0.83;\n"
"transition: opacity 0.6s;")

        self.verticalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btnCliente, self.btnProduto)
        QWidget.setTabOrder(self.btnProduto, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.txtNomeCli)
        QWidget.setTabOrder(self.txtNomeCli, self.txtCpfCli)
        QWidget.setTabOrder(self.txtCpfCli, self.txtEmailCli)
        QWidget.setTabOrder(self.txtEmailCli, self.txtEndCli)
        QWidget.setTabOrder(self.txtEndCli, self.txtFoneCli)
        QWidget.setTabOrder(self.txtFoneCli, self.txtBairroCli)
        QWidget.setTabOrder(self.txtBairroCli, self.cboCategCli)
        QWidget.setTabOrder(self.cboCategCli, self.btnSalvarCli)
        QWidget.setTabOrder(self.btnSalvarCli, self.tbWCliente)
        QWidget.setTabOrder(self.tbWCliente, self.btnAlterar)
        QWidget.setTabOrder(self.btnAlterar, self.btnExcluir)
        QWidget.setTabOrder(self.btnExcluir, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.btnSalvarProd)
        QWidget.setTabOrder(self.btnSalvarProd, self.tabWidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btnCliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.btnProduto.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.mCadastros), QCoreApplication.translate("MainWindow", u"Cadastros", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.mVendas), QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.lblMsg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">MENSAGENS</span></p></body></html>", None))
        self.btnExcluirMsg.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Logo</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic;\">Cadastro de Clientes</span><br /><span style=\" font-size:20pt; font-weight:600; font-style:italic;\">e Produtos</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Cadastro Clientes</span></p></body></html>", None))
        self.txtNomeCli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Cliente", None))
        self.txtCpfCli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txtEmailCli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">** Todos os campos s\u00e3o obrigat\u00f3rios</span></p></body></html>", None))
        self.txtEndCli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.txtFoneCli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fone", None))
        self.txtBairroCli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.cboCategCli.setItemText(0, QCoreApplication.translate("MainWindow", u"-- Categoria --", None))
        self.cboCategCli.setItemText(1, QCoreApplication.translate("MainWindow", u"Ouro", None))
        self.cboCategCli.setItemText(2, QCoreApplication.translate("MainWindow", u"Prata", None))
        self.cboCategCli.setItemText(3, QCoreApplication.translate("MainWindow", u"Bronze", None))

        self.btnSalvarCli.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabCli), QCoreApplication.translate("MainWindow", u"Cadastro Clientes", None))
        ___qtablewidgetitem = self.tbWCliente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tbWCliente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cpf", None));
        ___qtablewidgetitem2 = self.tbWCliente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tbWCliente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Endereco", None));
        ___qtablewidgetitem4 = self.tbWCliente.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fone", None));
        ___qtablewidgetitem5 = self.tbWCliente.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem6 = self.tbWCliente.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        self.btnAlterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabCliList), QCoreApplication.translate("MainWindow", u"Listar Clientes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Cadastro Produtos</span></p></body></html>", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Produto", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o R$", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quant. Estoque", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">** Todos os campos s\u00e3o obrigat\u00f3rios</span></p></body></html>", None))
        self.btnSalvarProd.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProd), QCoreApplication.translate("MainWindow", u"Cadastrar Produtos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProdList), QCoreApplication.translate("MainWindow", u"Listar Produtos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">@contatoeverton | Everton Oliveira - Criando Possibilidades</span></p></body></html>", None))
    # retranslateUi

