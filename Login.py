import Controller
from PyQt5 import QtCore, QtGui, QtWidgets
import RegistroNuevo


class Ui_MainWindow(object):

        def __init__(self) -> None:
                self.isConnected = False

        def openWindow(self):

                if self.isConnected:
                        self.destroy()
                        self.window = QtWidgets.QMainWindow()
                        self.ui = RegistroNuevo.Ui_SecondWindow(self.conexion)
                        self.ui.setupUi(self.window)
                        self.window.show()
                else:
                        self.mensajeError()

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(585, 403)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/proyecto/imagenes/iniciar-sesion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.585, y1:0.881, x2:1, y2:0, stop:0.352273 rgba(18, 19, 48, 255), stop:0.948864 rgba(0, 0, 117, 255));\n"
        "font: 10pt \"Malgun Gothic\";\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(250, 20, 331, 441))
                self.frame.setStyleSheet("background-color: rgb(5, 47, 69);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.lblusuario = QtWidgets.QLabel(self.frame)
                self.lblusuario.setGeometry(QtCore.QRect(50, 230, 71, 20))
                self.lblusuario.setStyleSheet("\n"
        "color: rgb(170, 255, 255);\n"
        "font: 75 12pt \"Arial Narrow\";\n"
        "\n"
        "")
                self.lblusuario.setObjectName("lblusuario")
                self.txtusuario = QtWidgets.QLineEdit(self.frame)
                self.txtusuario.setGeometry(QtCore.QRect(100, 230, 211, 20))
                font = QtGui.QFont()
                font.setFamily("MS Gothic")
                font.setPointSize(9)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.txtusuario.setFont(font)
                self.txtusuario.setAccessibleName("")
                self.txtusuario.setAccessibleDescription("")
                self.txtusuario.setAutoFillBackground(False)
                self.txtusuario.setStyleSheet("font: 9pt \"MS Gothic\";\n"
        "color:rgb(255, 255, 255);\n"
        "border-color: rgb(255, 0, 0);")
                self.txtusuario.setText("")
                self.txtusuario.setFrame(True)
                self.txtusuario.setDragEnabled(False)
                self.txtusuario.setReadOnly(False)
                self.txtusuario.setPlaceholderText("")
                self.txtusuario.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
                self.txtusuario.setClearButtonEnabled(True)
                self.txtusuario.setObjectName("txtusuario")
                self.iconcontra = QtWidgets.QLabel(self.frame)
                self.iconcontra.setGeometry(QtCore.QRect(10, 260, 31, 31))
                self.iconcontra.setAutoFillBackground(False)
                self.iconcontra.setText("")
                self.iconcontra.setPixmap(QtGui.QPixmap("imagenes/contrasena.png"))
                self.iconcontra.setScaledContents(True)
                self.iconcontra.setObjectName("iconcontra")
                self.iconusuario = QtWidgets.QLabel(self.frame)
                self.iconusuario.setGeometry(QtCore.QRect(20, 230, 21, 20))
                self.iconusuario.setStyleSheet("background-image: url(imagenes/contrasena.png);\n"
        "background-image: url(imagenes/usuario.png);")
                self.iconusuario.setText("")
                self.iconusuario.setPixmap(QtGui.QPixmap(":imagenes/usuario.png"))
                self.iconusuario.setScaledContents(True)
                self.iconusuario.setObjectName("iconusuario")
                self.btningresar = QtWidgets.QPushButton(self.frame, clicked = lambda: self.setupConnection())
                self.btningresar.setGeometry(QtCore.QRect(90, 330, 161, 31))
                self.btningresar.setStyleSheet("background-color: rgb(54, 183, 212);\n"
        "color:rgb(170, 255, 255)")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("imagenes/ingresar (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btningresar.setIcon(icon1)
                self.btningresar.setShortcut("")
                self.btningresar.setObjectName("btningresar")
                self.lblcontra = QtWidgets.QLabel(self.frame)
                self.lblcontra.setGeometry(QtCore.QRect(50, 270, 71, 20))
                self.lblcontra.setStyleSheet("\n"
        "color: rgb(170, 255, 255);\n"
        "font: 75 12pt \"Arial Narrow\";\n"
        "\n"
        "")
                self.lblcontra.setObjectName("lblcontra")
                self.imglogin = QtWidgets.QLabel(self.frame)
                self.imglogin.setGeometry(QtCore.QRect(100, 90, 131, 121))
                self.imglogin.setStyleSheet("background-image: url(imagenes/programador.png);")
                self.imglogin.setText("")
                self.imglogin.setPixmap(QtGui.QPixmap("imagenes/programador.png"))
                self.imglogin.setScaledContents(True)
                self.imglogin.setObjectName("imglogin")
                self.txtcontra = QtWidgets.QLineEdit(self.frame)
                self.txtcontra.setGeometry(QtCore.QRect(120, 270, 191, 20))
                font = QtGui.QFont()
                font.setFamily("MS Gothic")
                font.setPointSize(5)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.txtcontra.setFont(font)
                self.txtcontra.setAccessibleName("")
                self.txtcontra.setAccessibleDescription("")
                self.txtcontra.setAutoFillBackground(False)
                self.txtcontra.setStyleSheet("font:5pt \"MS Gothic\";\n"
        "color:rgb(255, 255, 255);\n"
        "border-color: rgb(255, 0, 0);")
                self.txtcontra.setText("")
                self.txtcontra.setFrame(True)
                self.txtcontra.setEchoMode(QtWidgets.QLineEdit.Password)
                self.txtcontra.setDragEnabled(False)
                self.txtcontra.setReadOnly(False)
                self.txtcontra.setPlaceholderText("")
                self.txtcontra.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
                self.txtcontra.setClearButtonEnabled(True)
                self.txtcontra.setObjectName("txtcontra")
                self.lbl = QtWidgets.QLabel(self.centralwidget)
                self.lbl.setEnabled(False)
                self.lbl.setGeometry(QtCore.QRect(10, 10, 571, 71))
                font = QtGui.QFont()
                font.setFamily("Arial Narrow")
                font.setPointSize(30)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                font.setKerning(True)
                self.lbl.setFont(font)
                self.lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.lbl.setStyleSheet("\n"
        "\n"
        "color: rgb(54, 183, 212);\n"
        "font: 75 30pt \"Arial Narrow\";\n"
        "\n"
        "\n"
        "\n"
        "")
                self.lbl.setFrameShape(QtWidgets.QFrame.Box)
                self.lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.lbl.setObjectName("lbl")
                self.imgcarro = QtWidgets.QLabel(self.centralwidget)
                self.imgcarro.setGeometry(QtCore.QRect(10, 90, 241, 291))
                self.imgcarro.setStyleSheet("")
                self.imgcarro.setText("")
                self.imgcarro.setPixmap(QtGui.QPixmap("imagenes/carros.png"))
                self.imgcarro.setScaledContents(True)
                self.imgcarro.setObjectName("imgcarro")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
                self.lblusuario.setText(_translate("MainWindow", "Usuario"))
                self.btningresar.setText(_translate("MainWindow", "Ingresar "))
                self.lblcontra.setText(_translate("MainWindow", "Contraseña"))
                self.lbl.setText(_translate("MainWindow", "Registro de Estacionamiento "))

        def setupConnection(self):
                try:
                        self.conexion = Controller.Conexion(self.txtusuario.text(), self.txtcontra.text())
                        self.isConnected = True
                except:
                        self.isConnected = False
                finally:
                        self.openWindow()

        def mensajeError(self):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Error en la conexión a la base de datos")
                msg.setInformativeText('Usuario y contraseña incorrectos.')
                msg.setWindowTitle("Error")
                msg.exec_()


