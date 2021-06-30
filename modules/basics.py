# -*- coding: utf-8 -*-

import sys, multimedia2, UI

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5 import uic

# ExampleUI = '../_uiFiles/example.ui'


def showVideos(button):
    print("Clicked!")
    multimedia2.run()


class MainDialog(QDialog, UI.Ui_Form):
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        # uic.loadUi(ExampleUI, self)
        self.setupUi(self)
        self.pushButton.clicked.connect(showVideos)


app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()
