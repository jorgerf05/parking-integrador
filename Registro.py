from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
import time, Controller, sys


class Ui_SecondWindow(object):
        def __init__(self, usuario:str, contra:str) -> None:
                self.user = usuario
                self.contra = contra
                try:
                        self.Conexion = Controller.Conexion(self.user, self.contra)
                except:
                        print("Usuario y contra incorrectos. Saliendo...")
                        sys.exit()
               
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(799, 479)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("imagenes/registro-en-linea.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
                self.scrollArea_2.setGeometry(QtCore.QRect(360, 0, 541, 451))
                self.scrollArea_2.setStyleSheet("")
                self.scrollArea_2.setWidgetResizable(True)
                self.scrollArea_2.setObjectName("scrollArea_2")
                self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
                self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 539, 449))
                self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
                self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
                self.label_2.setGeometry(QtCore.QRect(300, 20, 101, 91))
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap("imagenes/709011.png"))
                self.label_2.setScaledContents(True)
                self.label_2.setObjectName("label_2")
                self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
                self.tableWidget.setGeometry(QtCore.QRect(20, 130, 401, 201))
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setRowCount(4)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(3, item)
                self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
                self.label_8.setGeometry(QtCore.QRect(20, 40, 251, 51))
                self.label_8.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
        "color: rgb(0, 73, 107);")
                self.label_8.setObjectName("label_8")
                self.lcdNumber = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents_2)
                self.lcdNumber.setGeometry(QtCore.QRect(90, 340, 331, 71))
                self.lcdNumber.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(0, 0, 0);\n"
        "color: rgb(0, 85, 255);")

        #RELOJ
                self.lcdNumber.setDigitCount(8)
                self.lcdNumber.setObjectName("lcdNumber")
                self.timer = QTimer()
                self.timer.timeout.connect(self.showTime)
                self.timer.start(1000)
                self.showTime()
        #-----
                self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, 90, 361, 351))
                self.frame.setStyleSheet("background-color: rgb(0, 0, 43);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(40, 60, 261, 31))
                self.label_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "")
                self.label_4.setObjectName("label_4")
                self.txtnombre = QtWidgets.QLineEdit(self.frame)
                self.txtnombre.setGeometry(QtCore.QRect(130, 140, 211, 20))
                self.txtnombre.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 85, 127);")
                self.txtnombre.setObjectName("txtnombre")
                self.lblnombre = QtWidgets.QLabel(self.frame)
                self.lblnombre.setGeometry(QtCore.QRect(60, 140, 71, 16))
                self.lblnombre.setStyleSheet("font: 11pt \"Ebrima\";\n"
        "color: rgb(255, 255, 255);\n"
        "")
                self.lblnombre.setObjectName("lblnombre")
                self.txtdepartamento = QtWidgets.QLineEdit(self.frame)
                self.txtdepartamento.setGeometry(QtCore.QRect(130, 180, 211, 20))
                self.txtdepartamento.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 85, 127);")
                self.txtdepartamento.setObjectName("txtdepartamento")
                self.lbl_departamento = QtWidgets.QLabel(self.frame)
                self.lbl_departamento.setGeometry(QtCore.QRect(20, 180, 111, 16))
                self.lbl_departamento.setStyleSheet("font: 11pt \"Ebrima\";\n"
        "color: rgb(255, 255, 255);\n"
        "")
                self.lbl_departamento.setObjectName("lbl_departamento")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(50, 220, 81, 16))
                self.label_3.setStyleSheet("font: 11pt \"Ebrima\";\n"
        "color: rgb(255, 255, 255);\n"
        "")
                self.label_3.setObjectName("label_3")
                self.txtmatricula = QtWidgets.QLineEdit(self.frame)
                self.txtmatricula.setGeometry(QtCore.QRect(130, 220, 211, 20))
                self.txtmatricula.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 85, 127);")
                self.txtmatricula.setObjectName("txtmatricula")
                self.buttonguardar = QtWidgets.QPushButton(self.frame)
                self.buttonguardar.setGeometry(QtCore.QRect(40, 270, 121, 23))
                self.buttonguardar.setStyleSheet("background-color: rgb(0, 85, 127);\n"
        "color: rgb(255, 255, 255);\n"
        "")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("imagenes/salvar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.buttonguardar.setIcon(icon1)
                self.buttonguardar.setShortcut("")
                self.buttonguardar.setCheckable(False)
                self.buttonguardar.setFlat(False)
                self.buttonguardar.setObjectName("buttonguardar")
                self.buttonbuscar = QtWidgets.QPushButton(self.frame)
                self.buttonbuscar.setGeometry(QtCore.QRect(170, 270, 141, 21))
                self.buttonbuscar.setStyleSheet("background-color: rgb(0, 85, 127);\n"
        "color: rgb(255, 255, 255);\n"
        "")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("imagenes/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.buttonbuscar.setIcon(icon2)
                self.buttonbuscar.setObjectName("buttonbuscar")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, -10, 361, 131))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("imagenes/estacionamiento.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.toolBar = QtWidgets.QToolBar(MainWindow)
                self.toolBar.setObjectName("toolBar")
                MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Registro"))
                item = self.tableWidget.verticalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.tableWidget.verticalHeaderItem(1)
                item.setText(_translate("MainWindow", "Disponibilidad"))
                item = self.tableWidget.verticalHeaderItem(2)
                item.setText(_translate("MainWindow", "Horario de entrada"))
                item = self.tableWidget.verticalHeaderItem(3)
                item.setText(_translate("MainWindow", "Horario de Salida"))
                self.label_8.setText(_translate("MainWindow", "Zona de parking"))
                self.label_4.setText(_translate("MainWindow", "Informacion de usuario"))
                self.lblnombre.setText(_translate("MainWindow", "Nombre"))
                self.lbl_departamento.setText(_translate("MainWindow", "Departamento"))
                self.label_3.setText(_translate("MainWindow", "Matricula"))
                self.buttonguardar.setText(_translate("MainWindow", "Guardar registro "))
                self.buttonbuscar.setText(_translate("MainWindow", "Buscar lugares"))
                self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        def showTime(self):
                time = datetime.now()
                formatted_time = time.strftime("%I:%M:%S")
                self.lcdNumber.display(formatted_time)
        