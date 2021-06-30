# -*- coding: utf-8 -*-

import sys, multimedia2

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

ExampleUI = '../_uiFiles/example.ui'


def showVideos(button):
    print("Clicked!")
    multimedia2.run()


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ExampleUI, self)

        self.pushButton.clicked.connect(showVideos)


app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()
