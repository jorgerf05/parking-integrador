from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import ParkingWindow

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('ui/Login.ui', self)
        self.show()
    
    def changeUi(self):
        super(ParkingWindow, self).__init__()
        uic.loadUi('ui/Registro.ui')
        self.show()