# -*- coding: utf-8 -*-
import sys
import threading
from multiprocessing import Process

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

import example

ExampleUI = '../_uiFiles/example.ui'
Example3UI = '../_uiFiles/example3.ui'
Example4UI = '../_uiFiles/example4.ui'

playing = ["Run", "Stop"]
global a, b, c


def moveSubClass():
    print("Move Sub UI")
    widget.setCurrentIndex(widget.currentIndex() + 1)


def addVideo():
    print("Add Video")


def backButton():
    print("Move Back UI")
    widget.setCurrentIndex(widget.currentIndex() - 1)


def moveSSubClass():
    print("Move SSub Class")
    widget.setCurrentIndex(widget.currentIndex() + 2)


# main class
class MainWindow(QDialog):
    a = b = c = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(ExampleUI, self)
        self.show_pushButton.clicked.connect(self.showVideos)  # 동영상 재생
        self.exit_pushButton.clicked.connect(self.exitVideos)  # 동영상 종료
        self.move_pushButton.clicked.connect(moveSubClass)  # 다음 액티비티 이동
        self.calibration_pushButton.clicked.connect(moveSSubClass)  # calibration

        self.open_pushButton_1.clicked.connect(self.fileOpen1)  # 동영상1 선택
        self.stop_pushButton_1.clicked.connect(self.stopVideos1)  # 동영상1 일시정지
        self.open_pushButton_2.clicked.connect(self.fileOpen2)  # 동영상2 선택
        self.stop_pushButton_2.clicked.connect(self.stopVideos2)  # 동영상2 일시정지
        self.open_pushButton_3.clicked.connect(self.fileOpen3)  # 동영상3 선택
        self.stop_pushButton_3.clicked.connect(self.stopVideos3)  # 동영상3 일시정지

    def stopVideos1(self, state):
        self.a = (self.a + 1) % 2
        print("drone1 = " + playing[self.a])
        print("drone2 = " + playing[self.b])
        print("drone3 = " + playing[self.c])

    def stopVideos2(self, state):
        self.b = (self.b + 1) % 2
        print("drone1 = " + playing[self.a])
        print("drone2 = " + playing[self.b])
        print("drone3 = " + playing[self.c])

    def stopVideos3(self, state):
        self.c = (self.c + 1) % 2
        print("drone1 = " + playing[self.a])
        print("drone2 = " + playing[self.b])
        print("drone3 = " + playing[self.c])

    def fileOpen1(self):
        filename1 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_1')  # type == list
        filename_1 = '\n'.join(filename1[0])  # type == string
        self.plainTextEdit_1.appendPlainText(filename_1)
        print(filename_1)

    def fileOpen2(self):
        filename2 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_2')
        filename_2 = '\n'.join(filename2[0])
        self.plainTextEdit_2.appendPlainText(filename_2)
        print(filename_2)

    def fileOpen3(self):
        filename3 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_3')
        filename_3 = '\n'.join(filename3[0])
        self.plainTextEdit_3.appendPlainText(filename_3)
        print(filename_3)

    def exitVideos(self):
        print("Exit Videos")
        result_1, result_2, result_3 = self.getText()
        print("drone_1 : " + result_1)
        print("drone_2 : " + result_2)
        print("drone_3 : " + result_3)
        print(type(result_1))

    def getText(self):
        result_1 = self.plainTextEdit_1.toPlainText()
        result_2 = self.plainTextEdit_2.toPlainText()
        result_3 = self.plainTextEdit_3.toPlainText()
        return result_1, result_2, result_3

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:  # Main UI에서 ESC 클릭시 화면 날라가는 현상 발생
            print("ESC")
            pass  # pass 해둠으로써 그냥 넘어가게끔 만듦.
        elif e.key() == Qt.Key_F:
            print("F")
        elif e.key() == Qt.Key_N:
            print("N")

    def showVideos(self):
        print("Show Videos")
        try:
            result_1, result_2, result_3 = self.getText()
            print(result_1 + "\n" + result_2 + "\n" + result_3)
            t = Process(target=suum, args=(result_1, result_2, result_3))
            t.start()
            t.join()            
        except Exception as e:
            print(e)


def suum(result_1, result_2, result_3):
    example.run1(result_1)
    example.run2(result_2)
    example.run3(result_3)


# sub class
class subClass(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        loadUi(Example3UI, self)
        self.back_pushButton.clicked.connect(backButton)
        self.move_pushButton.clicked.connect(moveSubClass)


# sub sub class
class subSubClass(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        loadUi(Example4UI, self)
        self.back_pushButton.clicked.connect(backButton)
        self.setMouseTracking(True)
        # show UI the Drone Location

    def mouseMoveEvent(self, event):
        txtIn = "Inside Mouse 위치 ; x={0},y={1}".format(event.x(), event.y())
        txtOut = "Outside Mouse 위치 ; global={0},{1}".format(event.globalX(), event.globalY())
        self.drone_1_label.setText(txtIn)
        self.drone_2_label.setText(txtOut)

    def mouseButtonKind(self, buttons):
        if buttons & Qt.LeftButton:
            self.drone_3_label.setText("Mouse Click Left")
        if buttons & Qt.MidButton:
            self.drone_3_label.setText("Mouse Click Middle(Wheel)")
        if buttons & Qt.RightButton:
            self.drone_3_label.setText("Mouse Click Right")

    def mousePressEvent(self, e):
        self.mouseButtonKind(e.buttons())


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
