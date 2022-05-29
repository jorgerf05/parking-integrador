import sys, Login, Registro
from Persona import Persona
from Controller import Conexion
from PyQt5 import QtWidgets

def launchLogin():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def launchRegistro():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Registro.Ui_SecondWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def main():
    conex = Conexion("jorge","SisTemas!")
    persona = Persona("Alumno", "Aileen", "Sistemas", "01602266")
    conex.insertPersona(persona)
    conex.buscarMatricula("20760220")
    conex.buscarDepartamento("Sistemas")
    conex.buscarTipo("Alumno")
    
if __name__=="__main__":main()