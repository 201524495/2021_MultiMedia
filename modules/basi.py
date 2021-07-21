# -*- coding: utf-8 -*-
import UI, UI3, UI4
import example00
import sys
# import multimedia2

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import loadUi

# ExampleUI = '../_uiFiles/example.ui'
# Example3UI = '../_uiFiles/example3.ui'
# Example4UI = '../_uiFiles/example4.ui'


def moveSubClass():
    print("Move Sub UI")
    widget.setCurrentIndex(widget.currentIndex() + 1)


def stopVideos():
    print("Stop Videos")
    # multimedia2.cv2.waitKey(0)
    example00.cv2.waitKey(0)


def addVideo():
    print("Add Video")


def backButton():
    print("Move Back UI")
    widget.setCurrentIndex(widget.currentIndex() - 1)


def moveSSubClass():
    print("Move SSub Class")
    widget.setCurrentIndex(widget.currentIndex() + 2)


# main class
class MainWindow(QDialog, UI.Ui_Form):
    def __init__(self):
        # super(MainWindow, self).__init__()
        # loadUi(ExampleUI, self)
        QDialog.__init__(self, None)
        self.setupUi(self)

        self.show_pushButton.clicked.connect(self.showVideos)  # 동영상 재생
        self.stop_pushButton.clicked.connect(stopVideos)  # 동영상 일시정지
        self.exit_pushButton.clicked.connect(self.exitVideos)  # 동영상 종료
        self.addVideo_pushButton.clicked.connect(moveSSubClass)  # 1개 액티비티 뛰어 넘기
        self.move_pushButton.clicked.connect(moveSubClass)  # 다음 액티비티 이동
        self.open_pushButton_1.clicked.connect(self.fileOpen1)  # 동영상 선택
        self.open_pushButton_2.clicked.connect(self.fileOpen2)  # 동영상 선택
        self.open_pushButton_3.clicked.connect(self.fileOpen3)  # 동영상 선택

    def fileOpen1(self):
        filename1 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_1')  # type == list
        filename_1 = ''.join(filename1[0])  # type == string
        self.plainTextEdit_1.appendPlainText(filename_1)
        print(filename_1)

    def fileOpen2(self):
        filename2 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_2')
        filename_2 = ''.join(filename2[0])
        self.plainTextEdit_2.appendPlainText(filename_2)
        print(filename_2)

    def fileOpen3(self):
        filename3 = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Files For Drone_3')
        filename_3 = ''.join(filename3[0])
        self.plainTextEdit_3.appendPlainText(filename_3)
        print(filename_3)

    def exitVideos(self):
        print("Exit Videos")
        result_1, result_2, result_3 = self.getText()
        print("drone_1 : " + result_1)
        print("drone_2 : " + result_2)
        print("drone_3 : " + result_3)
        print(type(result_1))

    def showVideos(self):
        print("Show Videos")
        try:
            result_1, result_2, result_3 = self.getText()
            print(result_1)
            print(result_2)
            print(result_3)
            # multimedia2.run(result_1, result_2, result_3)
            example00.run(result_1, result_2, result_3)
        except Exception as e:
            print(e)

    def getText(self):
        result_1 = self.plainTextEdit_1.toPlainText()
        result_2 = self.plainTextEdit_2.toPlainText()
        result_3 = self.plainTextEdit_3.toPlainText()
        return result_1, result_2, result_3


# sub class
class subClass(QDialog, UI3.Ui_Form):
    def __init__(self):
        # super().__init__()
        # uic.loadUi(Example3UI, self)
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.back_pushButton.clicked.connect(backButton)
        self.move_pushButton.clicked.connect(moveSubClass)


# sub sub class
class subSubClass(QDialog, UI4.Ui_Form):
    def __init__(self):
        # super().__init__()
        # uic.loadUi(Example4UI, self)
        QDialog.__init__(self, None)
        self.setupUi(self)
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
