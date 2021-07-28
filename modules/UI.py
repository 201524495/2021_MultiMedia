# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_uiFiles/example.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(670, 400))
        self.plainTextEdit_1 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_1.setGeometry(QtCore.QRect(20, 70, 521, 81))
        self.plainTextEdit_1.setObjectName("plainTextEdit_1")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 160, 521, 81))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(20, 250, 521, 81))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")

        self.open_pushButton_1 = QtWidgets.QPushButton(Form)
        self.open_pushButton_1.setGeometry(QtCore.QRect(560, 80, 75, 23))
        self.open_pushButton_1.setObjectName("open_pushButton_1")
        self.open_pushButton_2 = QtWidgets.QPushButton(Form)
        self.open_pushButton_2.setGeometry(QtCore.QRect(560, 170, 75, 23))
        self.open_pushButton_2.setObjectName("open_pushButton_2")
        self.open_pushButton_3 = QtWidgets.QPushButton(Form)
        self.open_pushButton_3.setGeometry(QtCore.QRect(560, 250, 75, 23))
        self.open_pushButton_3.setObjectName("open_pushButton_3")

        self.show_pushButton = QtWidgets.QPushButton(Form)
        self.show_pushButton.setGeometry(QtCore.QRect(20, 30, 85, 23))
        self.show_pushButton.setObjectName("show_pushButton")
        self.addVideo_pushButton = QtWidgets.QPushButton(Form)
        self.addVideo_pushButton.setGeometry(QtCore.QRect(115, 30, 120, 23))
        self.addVideo_pushButton.setObjectName("addVideo_pushButton")
        self.move_pushButton = QtWidgets.QPushButton(Form)
        self.move_pushButton.setGeometry(QtCore.QRect(250, 30, 85, 23))
        self.move_pushButton.setObjectName("move_pushButton")
        self.exit_pushButton = QtWidgets.QPushButton(Form)
        self.exit_pushButton.setGeometry(QtCore.QRect(350, 30, 85, 23))
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(Form)
        self.stop_pushButton.setGeometry(QtCore.QRect(450, 30, 85, 23))
        self.stop_pushButton.setObjectName("stop_pushButton")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 360, 350, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.open_pushButton_1, self.open_pushButton_2)
        Form.setTabOrder(self.open_pushButton_2, self.open_pushButton_3)
        Form.setTabOrder(self.open_pushButton_3, self.show_pushButton)
        Form.setTabOrder(self.show_pushButton, self.move_pushButton)
        Form.setTabOrder(self.move_pushButton, self.plainTextEdit_2)
        Form.setTabOrder(self.plainTextEdit_2, self.addVideo_pushButton)
        Form.setTabOrder(self.addVideo_pushButton, self.plainTextEdit_3)
        Form.setTabOrder(self.plainTextEdit_3, self.exit_pushButton)
        Form.setTabOrder(self.exit_pushButton, self.stop_pushButton)
        Form.setTabOrder(self.stop_pushButton, self.plainTextEdit_1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open_pushButton_2.setText(_translate("Form", "Open File"))
        self.open_pushButton_3.setText(_translate("Form", "Open File"))
        self.move_pushButton.setText(_translate("Form", "Move Sub UI"))
        self.addVideo_pushButton.setText(_translate("Form", "Calibration Button"))
        self.open_pushButton_1.setText(_translate("Form", "Open File"))
        self.exit_pushButton.setText(_translate("Form", "Exit Videos"))
        self.stop_pushButton.setText(_translate("Form", "Stop Videos"))
        self.show_pushButton.setText(_translate("Form", "Show Videos"))
        self.label.setText(_translate("Form", "\"ESC\" 키 동영상 종료, \"space\"키 동영상 일시 정지 / 재생"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

