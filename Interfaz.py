from datetime import datetime
from functools import partial
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
import Conexion
from Persona import Persona

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/Login.ui', self) # Load the .ui file
        self._variablesLogin()
        self._conexionesLogin()
        self.show() # Show the GUI

    def _variablesLogin(self):
        self.isConnected = False
        self.txtUsuario = self.findChild(QtWidgets.QLineEdit, "txtusuario")
        self.txtContra = self.findChild(QtWidgets.QLineEdit, "txtcontra")
        self.btnIngresar = self.findChild(QtWidgets.QPushButton, "btningresar")
    
    def _variablesRegistro(self):
        self.lcdNumber = self.findChild(QtWidgets.QLCDNumber, "lcdNumber")
        self.txtMatricula = self.findChild(QtWidgets.QLineEdit, "txtmatricula")
        self.txtNombre = self.findChild(QtWidgets.QLineEdit,"txtnombre")
        self.cbxTipo = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.cbxEdificio = self.findChild(QtWidgets.QComboBox, "comboBox_2")
        self.btnRegistrar = self.findChild(QtWidgets.QPushButton, "btnregistro")
        self.btnLugar_1 = self.findChild(QtWidgets.QPushButton, "btnlugar1")
        self.btnLugar_2 = self.findChild(QtWidgets.QPushButton, "btnlugar2")
        self.btnLugar_3 = self.findChild(QtWidgets.QPushButton, "btnlugar3")

    def _variablesDialogo(self):
        self.txtOcupante = self.window.findChild(QtWidgets.QLineEdit, "txtocupante")
        self.btnOcupar = self.window.findChild(QtWidgets.QPushButton, "btnOcupar")
        self.btnLiberar = self.window.findChild(QtWidgets.QPushButton, "btnLiberar")
    
    def _conexionesLogin(self):
        self.btnIngresar.clicked.connect(self._login)

    def _conexionesRegistro(self):
        self.btnRegistrar.clicked.connect(self._registrarPersona)
        self.btnLugar_1.clicked.connect(partial(self._abrirDialogo, 1))
        self.btnLugar_2.clicked.connect(partial(self._abrirDialogo, 2))
        self.btnLugar_3.clicked.connect(partial(self._abrirDialogo, 3))
    
    def _conexionesDialogo(self):
        self.btnOcupar.clicked.connect(partial(self._ocuparLugar, self.activo))

    def _changeWindow(self):

        if self.isConnected:
            self.close()
            uic.loadUi('ui/registro.ui', self)
            self._variablesRegistro()
            self._conexionesRegistro()
            self._reloj()
            self.show()
        else:
            self._mensajeError("Error", "Error de conexión", "Usuario y contraseña incorrectos")
    
    def _abrirDialogo(self, id:int):

        if (id == 1):
            self.activo = 1
        elif (id == 2):
            self.activo = 2
        elif (id == 3):
            self.activo = 3
        print (self.activo)
        self.window = QtWidgets.QMainWindow()
        uic.loadUi('ui/dialogo.ui', self.window)
        #Desmadre de variables aqui
        self._variablesDialogo()
        self._conexionesDialogo()
        self.window.show()

    def _ocuparLugar(self, id:int):
        #Coidgo de verdad

        #Colores
        if (id == 1):
            self.btnLugar_1.setStyleSheet("background-color : yellow")
        elif (id == 2):
            self.btnLugar_2.setStyleSheet("background-color : yellow")
        elif (id == 3):
            self.btnLugar_3.setStyleSheet("background-color : yellow")

    def _login(self):
        try: 
            self.conexion = Conexion.Conexion(self.txtUsuario.text(), self.txtContra.text())
            self.isConnected = True
        except:
            self.isConnected = False
        finally: 
            self._changeWindow()

    def _mensajeError(self, titulo:str, texto:str, subtexto:str):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(texto)
            msg.setInformativeText(subtexto)
            msg.setWindowTitle(titulo)
            msg.exec_()
    
    def _reloj(self):
            self.lcdNumber.setDigitCount(8)
            self.timer = QTimer()
            self.timer.timeout.connect(self._showTime)
            self.timer.start(1000)
            self._showTime()

    def _showTime(self):
            time = datetime.now()
            formatted_time = time.strftime("%I:%M:%S")
            self.lcdNumber.display(formatted_time)

    def _registrarPersona(self):
            persona = Persona(self.cbxTipo.currentText(), self.txtNombre.text(), self.cbxEdificio.currentText(), self.txtMatricula.text())
            self.conexion.insertPersona(persona)