import sys, Interfaz, Conexion
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Interfaz.Ui()
    app.exec_()
    #conexion = Conexion.Conexion("jorge", "SisTemas!")
    #conexion.leerLugares()

if __name__=="__main__":main()