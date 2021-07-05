# -*- coding: utf-8 -*-


import multimedia2
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


TIME_LIMIT = 100
ExampleUI = '../_uiFiles/example.ui'
Example3UI = '../_uiFiles/example3.ui'
Example4UI = '../_uiFiles/example4.ui'
x1, y1, x2, y2, x3, y3 = multimedia2.initial()


def moveSubClass():
    print("Move Sub UI")
    widget.setCurrentIndex(widget.currentIndex() + 1)


def showVideos():
    print("Show Videos")
    multimedia2.run()


def addVideo():
    print("Add Video")


def backButton():
    print("Move Back UI")
    widget.setCurrentIndex(widget.currentIndex() - 1)


def moveSSubClass():
    print("Move SSub Class")
    widget.setCurrentIndex(widget.currentIndex() + 2)


# main class
class MainWindow(QDialog):  # , UI.Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(ExampleUI, self)
        self.show_pushButton.clicked.connect(showVideos)  # 동영상
        self.addVideo_pushButton.clicked.connect(moveSSubClass)  # 1개 액티비티 뛰어 넘기
        self.move_pushButton.clicked.connect(moveSubClass)  # 다음 액티비티 이동


# sub class
class subClass(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(Example3UI, self)
        self.back_pushButton.clicked.connect(backButton)
        self.move_pushButton.clicked.connect(moveSubClass)


# sub sub class
class subSubClass(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(Example4UI, self)
        self.back_pushButton.clicked.connect(backButton)
        self.setMouseTracking(True)
        # show UI the Drone Location

    def mouseMoveEvent(self, event):
        txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
        self.drone_1_label.setText(txt)
        self.drone_2_label.setText(txt)
        self.drone_3_label.setText(txt)


if __name__ == "__main__":
    # QApplication : The Class For Running Program
    app = QApplication(sys.argv)

    # Option UI Change
    widget = QtWidgets.QStackedWidget()

    # Create Layout Instance
    mainWindow = MainWindow()
    sub_class = subClass()
    subSub_class = subSubClass()

    # Add Widget & Sequence Open
    widget.addWidget(mainWindow)
    widget.addWidget(sub_class)
    widget.addWidget(subSub_class)

    # Show UI
    widget.show()

    # Running Event Loop
    app.exec_()