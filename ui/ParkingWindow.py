from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class ParkingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ParkingWindow, self).__init__()
        uic.loadUi('ui/Registro.ui', self)
        self.show()