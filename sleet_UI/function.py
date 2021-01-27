# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_funtion(object):

#  To open disclaimer
    def open_start(self):
        from start import Ui_start
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_start()
        self.ui.setupUi(self.window)
        self.window.show()


    def open_add(self):
        from add import Ui_add
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_add()
        self.ui.setupUi(self.window)
        self.window.show()

    def display(self):
        from display_timetable import Ui_time_table
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_time_table()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_delete(self):
        from delete import Ui_delete_2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_delete_2()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_loginpage(self):
        from loginpage import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, funtion):
        funtion.setObjectName("funtion")
        funtion.resize(700, 500)
        funtion.setMinimumSize(QtCore.QSize(700, 500))
        funtion.setMaximumSize(QtCore.QSize(700, 500))
        funtion.setStyleSheet("background-color: rgb(39, 19, 59)")
        self.centralwidget = QtWidgets.QWidget(funtion)
        self.centralwidget.setObjectName("centralwidget")
        self.instructionbtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_2.setGeometry(QtCore.QRect(250, 80, 191, 41))
        self.instructionbtn_2.setStyleSheet("QPushButton{\n"
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
"\n"
"background-color:rgb(83, 83, 83);\n"
"border-color: black;\n"
"border-width:5px\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.instructionbtn_2.setObjectName("instructionbtn_2")

        self.instructionbtn_2.clicked.connect(self.display)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 71))
        self.label.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"color: rgb(121, 121, 121);\n"
"font-size : 50px;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.instructionbtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_3.setGeometry(QtCore.QRect(250, 250, 191, 41))
        self.instructionbtn_3.setStyleSheet("QPushButton{\n"
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
        self.instructionbtn_3.setObjectName("instructionbtn_3")

        self.instructionbtn_3.clicked.connect(self.open_delete)
        self.instructionbtn_3.clicked.connect(funtion.close)

        self.instructionbtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_4.setGeometry(QtCore.QRect(250, 340, 191, 41))
        self.instructionbtn_4.setStyleSheet("QPushButton{\n"
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
"background-color:rgb(55, 179, 53);\n"
"border-color: black;\n"
"border-width:5px\n"
"\n"
"\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.instructionbtn_4.setObjectName("instructionbtn_4")

        self.instructionbtn_4.clicked.connect(self.open_loginpage)
        self.instructionbtn_4.clicked.connect(funtion.close)

        self.instructionbtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_5.setGeometry(QtCore.QRect(250, 170, 191, 41))
        self.instructionbtn_5.setStyleSheet("QPushButton{\n"
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
        self.instructionbtn_5.setObjectName("instructionbtn_5")

        self.instructionbtn_5.clicked.connect(self.open_add)
        self.instructionbtn_5.clicked.connect(funtion.close)

        self.instructionbtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.instructionbtn_6.setGeometry(QtCore.QRect(590, 450, 91, 31))
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

        self.instructionbtn_6.clicked.connect(self.open_start)
        self.instructionbtn_6.clicked.connect(funtion.close)

        funtion.setCentralWidget(self.centralwidget)

        self.retranslateUi(funtion)
        QtCore.QMetaObject.connectSlotsByName(funtion)

    def retranslateUi(self, funtion):
        _translate = QtCore.QCoreApplication.translate
        funtion.setWindowTitle(_translate("funtion", "Sleet"))
        self.instructionbtn_2.setText(_translate("funtion", "Display"))
        self.label.setText(_translate("funtion", "Sleet"))
        self.instructionbtn_3.setText(_translate("funtion", "Delete"))
        self.instructionbtn_4.setText(_translate("funtion", "Sleet"))
        self.instructionbtn_5.setText(_translate("funtion", "Add"))
        self.instructionbtn_6.setText(_translate("funtion", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    funtion = QtWidgets.QMainWindow()
    ui = Ui_funtion()
    ui.setupUi(funtion)
    funtion.show()
    sys.exit(app.exec_())
