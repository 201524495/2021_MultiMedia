# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_uiFiles/example4.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(437, 276)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.drone_1_label = QtWidgets.QLabel(Form)
        self.drone_1_label.setObjectName("drone_1_label")
        self.gridLayout.addWidget(self.drone_1_label, 1, 0, 1, 1)
        self.drone_2_label = QtWidgets.QLabel(Form)
        self.drone_2_label.setObjectName("drone_2_label")
        self.gridLayout.addWidget(self.drone_2_label, 2, 0, 1, 1)
        self.drone_3_label = QtWidgets.QLabel(Form)
        self.drone_3_label.setObjectName("drone_3_label")
        self.gridLayout.addWidget(self.drone_3_label, 3, 0, 1, 1)
        self.back_pushButton = QtWidgets.QPushButton(Form)
        self.back_pushButton.setObjectName("back_pushButton")
        self.gridLayout.addWidget(self.back_pushButton, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.drone_1_label.setText(_translate("Form", "Dron_1 Position"))
        self.drone_2_label.setText(_translate("Form", "Dron_2 Position"))
        self.drone_3_label.setText(_translate("Form", "Dron_3 Position"))
        self.back_pushButton.setText(_translate("Form", "Move Sub UI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

