# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete_2(object):

    def open_function(self):
        from function import Ui_funtion
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_funtion()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, delete_2):
        delete_2.setObjectName("delete_2")
        delete_2.resize(600, 500)
        delete_2.setMinimumSize(QtCore.QSize(600, 500))
        delete_2.setMaximumSize(QtCore.QSize(600, 500))
        delete_2.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.centralwidget = QtWidgets.QWidget(delete_2)
        self.centralwidget.setObjectName("centralwidget")
        self.instructionbtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_2.setGeometry(QtCore.QRect(90, 150, 191, 41))
        self.instructionbtn_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(156, 72, 33);\n"
"border-color: grey;\n"
"border-radius:10px ;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"font-weight: bold;\n"
"transition: all 0.5s;\n"
"font-size:13px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(156, 72, 33);\n"
"border-color: white;\n"
"border-width:5px\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.instructionbtn_2.setObjectName("instructionbtn_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 71))
        self.label.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"color: rgb(121, 121, 121);\n"
"font-size : 50px;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.instructionbtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_3.setGeometry(QtCore.QRect(90, 310, 191, 41))
        self.instructionbtn_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(156, 72, 33);\n"
"border-color: grey;\n"
"border-radius:10px ;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"font-weight: bold;\n"
"transition: all 0.5s;\n"
"font-size:13px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(156, 72, 33);\n"
"border-color: white;\n"
"border-width:5px\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.instructionbtn_3.setObjectName("instructionbtn_3")
        self.instructionbtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_4.setGeometry(QtCore.QRect(330, 150, 191, 41))
        self.instructionbtn_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(156, 72, 33);\n"
"border-color: grey;\n"
"border-radius:10px ;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"font-weight: bold;\n"
"transition: all 0.5s;\n"
"font-size:13px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(156, 72, 33);\n"
"border-color: white;\n"
"border-width:5px\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.instructionbtn_4.setObjectName("instructionbtn_4")
        self.instructionbtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_5.setGeometry(QtCore.QRect(330, 310, 191, 41))
        self.instructionbtn_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(156, 72, 33);\n"
"border-color: grey;\n"
"border-radius:10px ;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"font-weight: bold;\n"
"transition: all 0.5s;\n"
"font-size:13px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(156, 72, 33);\n"
"border-color: white;\n"
"border-width:5px\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.instructionbtn_5.setObjectName("instructionbtn_5")
        self.instructionbtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_6.setGeometry(QtCore.QRect(490, 450, 91, 31))
        self.instructionbtn_6.setStyleSheet("QPushButton{\n"
"background-color: rgb(115, 129, 241);\n"
"border-color: grey;\n"
"border-radius:10px ;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"font-weight: bold;\n"
"transition: all 0.5s;\n"
"font-size:13px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(83, 83, 83);\n"
"border-color: black;\n"
"border-width:5px\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.instructionbtn_6.setObjectName("instructionbtn_6")

        self.instructionbtn_6.clicked.connect(self.open_function)
        self.instructionbtn_6.clicked.connect(delete_2.close)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 80, 71, 31))
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"color: rgb(121, 121, 121);\n"
"font-size : 25px;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        delete_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(delete_2)
        QtCore.QMetaObject.connectSlotsByName(delete_2)

    def retranslateUi(self, delete_2):
        _translate = QtCore.QCoreApplication.translate
        delete_2.setWindowTitle(_translate("delete_2", "Sleet"))
        self.instructionbtn_2.setText(_translate("delete_2", "Time-Table"))
        self.label.setText(_translate("delete_2", "Sleet"))
        self.instructionbtn_3.setText(_translate("delete_2", "Subject-List"))
        self.instructionbtn_4.setText(_translate("delete_2", "Custom-Day"))
        self.instructionbtn_5.setText(_translate("delete_2", "Display"))
        self.instructionbtn_6.setText(_translate("delete_2", "Back"))
        self.label_2.setText(_translate("delete_2", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_2 = QtWidgets.QMainWindow()
    ui = Ui_delete_2()
    ui.setupUi(delete_2)
    delete_2.show()
    sys.exit(app.exec_())
