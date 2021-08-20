# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

import example
import example00
import tapUI
import UI4

ExampleTabUI = '../_uiFiles/tapUI.ui'
Example4UI = '../_uiFiles/example4.ui'

playing = ["300*500", "500*300"]
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
class MainWindow(QDialog, tapUI.Ui_Form):
    # 챕터 1(_0x), 2(_1x), 3(_2x), 4(_3x) , 드론 1(_x1) , 2(_x2) , 3(_x3)
    _01 = _02 = _03 = _11 = _12 = _13 = _21 = _22 = _23 = _31 = _32 = _33 = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        # loadUi(ExampleTabUI, self)

        QDialog.__init__(self, None)
        self.setupUi(self)

        self.calibration_pushButton_00.clicked.connect(moveSSubClass)  # calibration

        self.exit_pushButton_00.clicked.connect(
            lambda state, button=self.exit_pushButton_00: self.exitVideos(state, button))  # 동영상 종료
        self.exit_pushButton_10.clicked.connect(
            lambda state, button=self.exit_pushButton_10: self.exitVideos(state, button))  # 동영상 종료
        self.exit_pushButton_20.clicked.connect(
            lambda state, button=self.exit_pushButton_20: self.exitVideos(state, button))  # 동영상 종료
        self.exit_pushButton_30.clicked.connect(
            lambda state, button=self.exit_pushButton_30: self.exitVideos(state, button))  # 동영상 종료

        self.show_pushButton_00.clicked.connect(
            lambda state, button=self.show_pushButton_00: self.showVideos(state, button))  # chapter_1 동영상 재생
        self.show_pushButton_10.clicked.connect(
            lambda state, button=self.show_pushButton_10: self.showVideos(state, button))  # chapter_2 동영상 재생
        self.show_pushButton_20.clicked.connect(
            lambda state, button=self.show_pushButton_20: self.showVideos(state, button))  # chapter_3 동영상 재생
        self.show_pushButton_30.clicked.connect(
            lambda state, button=self.show_pushButton_30: self.showVideos(state, button))  # chapter_4 동영상 재생

        self.open_pushButton_01.clicked.connect(
            lambda state, button=self.open_pushButton_01: self.fileOpen(state, button))  # chapter_1 동영상1 선택
        self.open_pushButton_02.clicked.connect(
            lambda state, button=self.open_pushButton_02: self.fileOpen(state, button))  # chapter_1 동영상2 선택
        self.open_pushButton_03.clicked.connect(
            lambda state, button=self.open_pushButton_03: self.fileOpen(state, button))  # chapter_1 동영상3 선택
        self.open_pushButton_11.clicked.connect(
            lambda state, button=self.open_pushButton_11: self.fileOpen(state, button))  # chapter_2 동영상1 선택
        self.open_pushButton_12.clicked.connect(
            lambda state, button=self.open_pushButton_12: self.fileOpen(state, button))  # chapter_2 동영상2 선택
        self.open_pushButton_13.clicked.connect(
            lambda state, button=self.open_pushButton_13: self.fileOpen(state, button))  # chapter_2 동영상3 선택
        self.open_pushButton_21.clicked.connect(
            lambda state, button=self.open_pushButton_21: self.fileOpen(state, button))  # chapter_3 동영상1 선택
        self.open_pushButton_22.clicked.connect(
            lambda state, button=self.open_pushButton_22: self.fileOpen(state, button))  # chapter_3 동영상2 선택
        self.open_pushButton_23.clicked.connect(
            lambda state, button=self.open_pushButton_23: self.fileOpen(state, button))  # chapter_3 동영상3 선택
        self.open_pushButton_31.clicked.connect(
            lambda state, button=self.open_pushButton_31: self.fileOpen(state, button))  # chapter_3 동영상1 선택
        self.open_pushButton_32.clicked.connect(
            lambda state, button=self.open_pushButton_32: self.fileOpen(state, button))  # chapter_3 동영상2 선택
        self.open_pushButton_33.clicked.connect(
            lambda state, button=self.open_pushButton_33: self.fileOpen(state, button))  # chapter_3 동영상3 선택

        self.checkBox_01.clicked.connect(
            lambda state, button=self.checkBox_01: self.changeSize(state, button))  # chapter_1 동영상1 일시정지
        self.checkBox_02.clicked.connect(
            lambda state, button=self.checkBox_02: self.changeSize(state, button))  # chapter_1 동영상2 일시정지
        self.checkBox_03.clicked.connect(
            lambda state, button=self.checkBox_03: self.changeSize(state, button))  # chapter_1 동영상3 일시정지
        self.checkBox_11.clicked.connect(
            lambda state, button=self.checkBox_11: self.changeSize(state, button))  # chapter_2 동영상1 일시정지
        self.checkBox_12.clicked.connect(
            lambda state, button=self.checkBox_12: self.changeSize(state, button))  # chapter_2 동영상2 일시정지
        self.checkBox_13.clicked.connect(
            lambda state, button=self.checkBox_13: self.changeSize(state, button))  # chapter_2 동영상3 일시정지
        self.checkBox_21.clicked.connect(
            lambda state, button=self.checkBox_21: self.changeSize(state, button))  # chapter_3 동영상1 일시정지
        self.checkBox_22.clicked.connect(
            lambda state, button=self.checkBox_22: self.changeSize(state, button))  # chapter_3 동영상2 일시정지
        self.checkBox_23.clicked.connect(
            lambda state, button=self.checkBox_23: self.changeSize(state, button))  # chapter_3 동영상3 일시정지
        self.checkBox_31.clicked.connect(
            lambda state, button=self.checkBox_31: self.changeSize(state, button))  # chapter_3 동영상1 일시정지
        self.checkBox_32.clicked.connect(
            lambda state, button=self.checkBox_32: self.changeSize(state, button))  # chapter_3 동영상2 일시정지
        self.checkBox_33.clicked.connect(
            lambda state, button=self.checkBox_33: self.changeSize(state, button))  # chapter_3 동영상3 일시정지

    def changeSize(self, state, button):
        if button == self.checkBox_01:  # chapter_1 drone_1
            self._01 = (self._01 + 1) % 2
            print("drone1_1 = " + playing[self._01])
        if button == self.checkBox_02:  # chapter_1 drone_2
            self._02 = (self._02 + 1) % 2
            print("drone1_2 = " + playing[self._02])
        if button == self.checkBox_03:  # chapter_1 drone_3
            self._03 = (self._03 + 1) % 2
            print("drone1_3 = " + playing[self._03])

        if button == self.checkBox_11:  # chapter_2 drone_1
            self._11 = (self._11 + 1) % 2
            print("drone2_1 = " + playing[self._11])
        if button == self.checkBox_12:  # chapter_2 drone_2
            self._12 = (self._12 + 1) % 2
            print("drone2_2 = " + playing[self._12])
        if button == self.checkBox_13:  # chapter_2 drone_3
            self._13 = (self._13 + 1) % 2
            print("drone2_3 = " + playing[self._13])

        if button == self.checkBox_21:  # chapter_3 drone_1
            self._21 = (self._21 + 1) % 2
            print("drone3_1 = " + playing[self._21])
        if button == self.checkBox_22:  # chapter_3 drone_2
            self._22 = (self._22 + 1) % 2
            print("drone3_2 = " + playing[self._22])
        if button == self.checkBox_23:  # chapter_3 drone_3
            self._23 = (self._23 + 1) % 2
            print("drone3_3 = " + playing[self._23])

        if button == self.checkBox_31:  # chapter_4 drone_1
            self._31 = (self._31 + 1) % 2
            print("drone4_1 = " + playing[self._31])
        if button == self.checkBox_32:  # chapter_4 drone_2
            self._32 = (self._32 + 1) % 2
            print("drone4_2 = " + playing[self._32])
        if button == self.checkBox_33:  # chapter_4 drone_3
            self._33 = (self._33 + 1) % 2
            print("drone4_3 = " + playing[self._33])

    def fileOpen(self, state, button):  # chapter_1
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

        if button == self.open_pushButton_31:
            filename31 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_1')  # type == list
            filename_31 = '\n'.join(filename31[0])  # type == string
            self.plainTextEdit_31.appendPlainText(filename_31)
            print(filename_31)
        if button == self.open_pushButton_32:
            filename32 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_2')
            filename_32 = '\n'.join(filename32[0])
            self.plainTextEdit_32.appendPlainText(filename_32)
            print(filename_32)
        if button == self.open_pushButton_33:
            filename33 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_3')
            filename_33 = '\n'.join(filename33[0])
            self.plainTextEdit_33.appendPlainText(filename_33)
            print(filename_33)

    def exitVideos(self, state, button):  # ???
        print("Exit Videos")
        if button == self.exit_pushButton_00:
            sys.exit(QCoreApplication.instance().quit)

        if button == self.exit_pushButton_10:
            sys.exit(QCoreApplication.instance().quit)

        if button == self.exit_pushButton_20:
            sys.exit(QCoreApplication.instance().quit)

        if button == self.exit_pushButton_30:
            sys.exit(QCoreApplication.instance().quit)

    def closeEvent(self, event):
        print("event")
        from PyQt5 import QtGui
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:  # Main UI 에서 ESC 클릭시 화면 날라가는 현상 발생
            print("ESC")
            pass  # pass 해둠으로써 그냥 넘어가게끔 만듦.
        elif e.key() == Qt.Key_F:
            print("F")
        elif e.key() == Qt.Key_N:
            print("N")

    def showVideos(self, state, button):
        result_1 = result_2 = result_3 = ""
        if button == self.show_pushButton_00:
            print("Show Videos")
            try:
                result_1, result_2, result_3 = self.plainTextEdit_01.toPlainText(), self.plainTextEdit_02.toPlainText(), self.plainTextEdit_03.toPlainText()
                print(result_1 + "\n" + result_2 + "\n" + result_3)
                PlayVideo(result_1, result_2, result_3, self._01, self._02, self._03)
            except Exception as e:
                print(e)

        if button == self.show_pushButton_10:
            print("Show Videos")
            try:
                result_1, result_2, result_3 = self.plainTextEdit_11.toPlainText(), self.plainTextEdit_12.toPlainText(), self.plainTextEdit_13.toPlainText()
                print(result_1 + "\n" + result_2 + "\n" + result_3)
                PlayVideo(result_1, result_2, result_3, self._11, self._12, self._13)
            except Exception as e:
                print(e)

        if button == self.show_pushButton_20:
            print("Show Videos")
            try:
                result_1, result_2, result_3 = self.plainTextEdit_21.toPlainText(), self.plainTextEdit_22.toPlainText(), self.plainTextEdit_23.toPlainText()
                print(result_1 + "\n" + result_2 + "\n" + result_3)
                PlayVideo(result_1, result_2, result_3, self._21, self._22, self._23)
            except Exception as e:
                print(e)

        if button == self.show_pushButton_30:
            print("Show Videos")
            try:
                result_1, result_2, result_3 = self.plainTextEdit_31.toPlainText(), self.plainTextEdit_32.toPlainText(), self.plainTextEdit_33.toPlainText()
                print(result_1 + "\n" + result_2 + "\n" + result_3)
                PlayVideo(result_1, result_2, result_3, self._31, self._32, self._33)
            except Exception as e:
                print(e)


def PlayVideo(video_1, video_2, video_3, drone_1, drone_2, drone_3):
    example00.run(video_1, video_2, video_3, drone_1, drone_2, drone_3)


# sub sub class
class subSubClass(QDialog, UI4.Ui_Form):
    def __init__(self):
        QDialog.__init__(self, None)
        # loadUi(Example4UI, self)
        self.setupUi(self)

        self.back_pushButton.clicked.connect(backButton)
        self.setMouseTracking(True)
        # show UI the Drone Location

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:  # Main UI 에서 ESC 클릭시 화면 날라가는 현상 발생
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
