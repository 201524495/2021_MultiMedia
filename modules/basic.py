# -*- coding: utf-8 -*-
import sys
import threading
from multiprocessing import Process

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

import example
from modules import example00

ExampleUI = '../_uiFiles/example.ui'
ExampleTabUI = '../_uiFiles/tapUI.ui'
Example3UI = '../_uiFiles/example3.ui'
Example4UI = '../_uiFiles/example4.ui'

playing = ["Run", "Stop"]
global a, b, c


def addVideo():
    print("Add Video")


def backButton():
    print("Move Back UI")
    widget.setCurrentIndex(widget.currentIndex() - 1)


def moveSSubClass():
    print("Move Calibration Class")
    widget.setCurrentIndex(widget.currentIndex() + 1)


# main class
class MainWindow(QDialog):
    a_01 = b_01 = c_01 = a_02 = b_02 = c_02 = a_03 = b_03 = c_03 = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(ExampleTabUI, self)

        self.exit_pushButton_00.clicked.connect(lambda state, button=self.exit_pushButton_00: self.exitVideos(state, button))  # 동영상 종료
        self.exit_pushButton_10.clicked.connect(lambda state, button=self.exit_pushButton_10: self.exitVideos(state, button))  # 동영상 종료
        self.exit_pushButton_20.clicked.connect(lambda state, button=self.exit_pushButton_20: self.exitVideos(state, button))  # 동영상 종료
        self.calibration_pushButton_00.clicked.connect(moveSSubClass)  # calibration

        self.show_pushButton_00.clicked.connect(lambda state, button=self.show_pushButton_00: self.showVideos(state, button))  # chapter_1 동영상 재생
        self.show_pushButton_10.clicked.connect(lambda state, button=self.show_pushButton_10: self.showVideos(state, button))  # chapter_2 동영상 재생
        self.show_pushButton_20.clicked.connect(lambda state, button=self.show_pushButton_20: self.showVideos(state, button))  # chapter_3 동영상 재생

        self.open_pushButton_01.clicked.connect(lambda state, button=self.open_pushButton_01: self.fileOpen1(state, button))  # chapter_1 동영상1 선택
        self.open_pushButton_02.clicked.connect(lambda state, button=self.open_pushButton_02: self.fileOpen1(state, button))  # chapter_1 동영상2 선택
        self.open_pushButton_03.clicked.connect(lambda state, button=self.open_pushButton_03: self.fileOpen1(state, button))  # chapter_1 동영상3 선택
        self.open_pushButton_11.clicked.connect(lambda state, button=self.open_pushButton_11: self.fileOpen2(state, button))  # chapter_2 동영상1 선택
        self.open_pushButton_12.clicked.connect(lambda state, button=self.open_pushButton_12: self.fileOpen2(state, button))  # chapter_2 동영상2 선택
        self.open_pushButton_13.clicked.connect(lambda state, button=self.open_pushButton_13: self.fileOpen2(state, button))  # chapter_2 동영상3 선택
        self.open_pushButton_21.clicked.connect(lambda state, button=self.open_pushButton_21: self.fileOpen3(state, button))  # chapter_3 동영상1 선택
        self.open_pushButton_22.clicked.connect(lambda state, button=self.open_pushButton_22: self.fileOpen3(state, button))  # chapter_3 동영상2 선택
        self.open_pushButton_23.clicked.connect(lambda state, button=self.open_pushButton_23: self.fileOpen3(state, button))  # chapter_3 동영상3 선택

        self.stop_pushButton_01.clicked.connect(lambda state, button=self.stop_pushButton_01: self.stopVideos1(state, button))  # chapter_1 동영상1 일시정지
        self.stop_pushButton_02.clicked.connect(lambda state, button=self.stop_pushButton_02: self.stopVideos2(state, button))  # chapter_1 동영상2 일시정지
        self.stop_pushButton_03.clicked.connect(lambda state, button=self.stop_pushButton_03: self.stopVideos3(state, button))  # chapter_1 동영상3 일시정지
        self.stop_pushButton_11.clicked.connect(lambda state, button=self.stop_pushButton_11: self.stopVideos1(state, button))  # chapter_2 동영상1 일시정지
        self.stop_pushButton_12.clicked.connect(lambda state, button=self.stop_pushButton_12: self.stopVideos2(state, button))  # chapter_2 동영상2 일시정지
        self.stop_pushButton_13.clicked.connect(lambda state, button=self.stop_pushButton_13: self.stopVideos3(state, button))  # chapter_2 동영상3 일시정지
        self.stop_pushButton_21.clicked.connect(lambda state, button=self.stop_pushButton_21: self.stopVideos1(state, button))  # chapter_3 동영상1 일시정지
        self.stop_pushButton_22.clicked.connect(lambda state, button=self.stop_pushButton_22: self.stopVideos2(state, button))  # chapter_3 동영상2 일시정지
        self.stop_pushButton_23.clicked.connect(lambda state, button=self.stop_pushButton_23: self.stopVideos3(state, button))  # chapter_3 동영상3 일시정지

    def stopVideos1(self, state, button):
        if button == self.stop_pushButton_01:  # chapter_1 drone_1
            self.a_01 = (self.a_01 + 1) % 2
            print("drone1_1 = " + playing[self.a_01])
            return self.a_01
        if button == self.stop_pushButton_11:  # chapter_2 drone_1
            self.a_02 = (self.a_02 + 1) % 2
            print("drone2_1 = " + playing[self.a_02])
            return self.a_02
        if button == self.stop_pushButton_21:  # chapter_3 drone_1
            self.a_03 = (self.a_03 + 1) % 2
            print("drone3_1 = " + playing[self.a_03])
            return self.a_03

    def stopVideos2(self, state, button):
        if button == self.stop_pushButton_02:  # chapter_1 drone_2
            self.b_01 = (self.b_01 + 1) % 2
            print("drone1_2 = " + playing[self.b_01])
            return self.b_01
        if button == self.stop_pushButton_12:  # chapter_2 drone_2
            self.b_02 = (self.b_02 + 1) % 2
            print("drone2_2 = " + playing[self.b_02])
            return self.b_02
        if button == self.stop_pushButton_22:  # chapter_3 drone_2
            self.b_03 = (self.b_03 + 1) % 2
            print("drone3_2 = " + playing[self.b_03])
            return self.b_03

    def stopVideos3(self, state, button):
        if button == self.stop_pushButton_03:  # chapter_1 drone_3
            self.c_01 = (self.c_01 + 1) % 2
            print("drone1_3 = " + playing[self.c_01])
            return self.c_01
        if button == self.stop_pushButton_13:  # chapter_2 drone_3
            self.c_02 = (self.c_02 + 1) % 2
            print("drone2_3 = " + playing[self.c_02])
            return self.c_02
        if button == self.stop_pushButton_23:  # chapter_3 drone_3
            self.c_03 = (self.c_03 + 1) % 2
            print("drone3_3 = " + playing[self.c_03])
            return self.c_03

    def fileOpen1(self, state, button):  # chapter_1
        if button == self.open_pushButton_01:
            filename01 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_1')  # type == list
            filename_01 = '\n'.join(filename01[0])  # type == string
            self.plainTextEdit_01.appendPlainText(filename_01)
            print(filename_01)
        if button == self.open_pushButton_02:
            filename02 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_2')
            filename_02 = '\n'.join(filename02[0])
            self.plainTextEdit_02.appendPlainText(filename_02)
            print(filename_02)
        if button == self.open_pushButton_03:
            filename03 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_3')
            filename_03 = '\n'.join(filename03[0])
            self.plainTextEdit_03.appendPlainText(filename_03)
            print(filename_03)

    def fileOpen2(self, state, button):  # chapter_2
        if button == self.open_pushButton_11:
            filename11 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_1')  # type == list
            filename_11 = '\n'.join(filename11[0])  # type == string
            self.plainTextEdit_11.appendPlainText(filename_11)
            print(filename_11)
        if button == self.open_pushButton_12:
            filename12 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_2')
            filename_12 = '\n'.join(filename12[0])
            self.plainTextEdit_12.appendPlainText(filename_12)
            print(filename_12)
        if button == self.open_pushButton_13:
            filename13 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_3')
            filename_13 = '\n'.join(filename13[0])
            self.plainTextEdit_13.appendPlainText(filename_13)
            print(filename_13)

    def fileOpen3(self, state, button):  # chapter_3
        if button == self.open_pushButton_21:
            filename21 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_1')  # type == list
            filename_21 = '\n'.join(filename21[0])  # type == string
            self.plainTextEdit_21.appendPlainText(filename_21)
            print(filename_21)
        if button == self.open_pushButton_22:
            filename22 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_2')
            filename_22 = '\n'.join(filename22[0])
            self.plainTextEdit_22.appendPlainText(filename_22)
            print(filename_22)
        if button == self.open_pushButton_23:
            filename23 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_3')
            filename_23 = '\n'.join(filename23[0])
            self.plainTextEdit_23.appendPlainText(filename_23)
            print(filename_23)

    def exitVideos(self, state, button):  # ???
        print("Exit Videos")
        if button == self.exit_pushButton_00:
            result_1, result_2, result_3 = self.plainTextEdit_01.toPlainText(), self.plainTextEdit_02.toPlainText(), self.plainTextEdit_03.toPlainText()
            print(result_1, result_2, result_3)
        if button == self.exit_pushButton_10:
            result_1, result_2, result_3 = self.plainTextEdit_11.toPlainText(), self.plainTextEdit_12.toPlainText(), self.plainTextEdit_13.toPlainText()
            print(result_1, result_2, result_3)
        if button == self.exit_pushButton_20:
            result_1, result_2, result_3 = self.plainTextEdit_21.toPlainText(), self.plainTextEdit_22.toPlainText(), self.plainTextEdit_23.toPlainText()
            print(result_1, result_2, result_3)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:  # Main UI에서 ESC 클릭시 화면 날라가는 현상 발생
            print("ESC")
            pass  # pass 해둠으로써 그냥 넘어가게끔 만듦.
        elif e.key() == Qt.Key_F:
            print("F")
        elif e.key() == Qt.Key_N:
            print("N")

    def showVideos(self, state, button):
        if button == self.show_pushButton_00:
            print("Show Videos")
            try:
                result_1, result_2, result_3 = self.plainTextEdit_01.toPlainText(), self.plainTextEdit_02.toPlainText(), self.plainTextEdit_03.toPlainText()
                print(result_1 + "\n" + result_2 + "\n" + result_3)
                t = Process(target=PlayVideo, args=(result_1, result_2, result_3))
                t.start()
                t.join()
            except Exception as e:
                print(e)

        if button == self.show_pushButton_10:
            print("Show Videos")
            try:
                result_1, result_2, result_3 = self.plainTextEdit_11.toPlainText(), self.plainTextEdit_12.toPlainText(), self.plainTextEdit_13.toPlainText()
                print(result_1 + "\n" + result_2 + "\n" + result_3)
                t = Process(target=PlayVideo, args=(result_1, result_2, result_3))
                t.start()
                t.join()
            except Exception as e:
                print(e)

        if button == self.show_pushButton_20:
            print("Show Videos")
            try:
                result_1, result_2, result_3 = self.plainTextEdit_21.toPlainText(), self.plainTextEdit_22.toPlainText(), self.plainTextEdit_23.toPlainText()
                print(result_1 + "\n" + result_2 + "\n" + result_3)
                # t = Process(target=PlayVideo, args=(result_1, result_2, result_3))
                # t.start()
                # t.join()
                PlayVideo(result_1, result_2, result_3)
            except Exception as e:
                print(e)


def PlayVideo(video_1, video_2, video_3):
    # example.run1(video_1)
    # example.run2(video_2)
    # example.run3(video_3)
    example00.run(video_1, video_2, video_3)


# sub sub class
class subSubClass(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        loadUi(Example4UI, self)
        self.back_pushButton.clicked.connect(backButton)
        self.setMouseTracking(True)
        # show UI the Drone Location

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:  # Main UI에서 ESC 클릭시 화면 날라가는 현상 발생
            print("ESC")
            pass  # pass 해둠으로써 그냥 넘어가게끔 만듦.
        elif e.key() == Qt.Key_F:
            print("F")
        elif e.key() == Qt.Key_N:
            print("N")

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
    subSub_class = subSubClass()

    # Add Widget & Sequence Open
    widget.addWidget(mainWindow)
    widget.addWidget(subSub_class)

    # Show UI
    widget.show()

    # Running Event Loop
    app.exec_()
