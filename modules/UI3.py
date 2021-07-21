# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_uiFiles/example3.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.back_pushButton = QtWidgets.QPushButton(Form)
        self.back_pushButton.setObjectName("back_pushButton")
        self.gridLayout.addWidget(self.back_pushButton, 2, 0, 1, 1)
        self.move_pushButton = QtWidgets.QPushButton(Form)
        self.move_pushButton.setObjectName("move_pushButton")
        self.gridLayout.addWidget(self.move_pushButton, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back_pushButton.setText(_translate("Form", "Move Main UI"))
        self.move_pushButton.setText(_translate("Form", "Move SubSub UI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

