import sys, Interfaz
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Interfaz.Ui()
    app.exec_()

if __name__=="__main__":main()