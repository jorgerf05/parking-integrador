import sys, Login, Registro, prueba
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
    ui = Registro.Ui_SecondWindow("jorge","SisTemas!")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = prueba.Ui() # Create an instance of our class
    app.exec_() # Start the application

if __name__=="__main__":main()