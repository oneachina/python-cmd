# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ccmd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1535, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1521, 721))
        self.frame.setStyleSheet("QFrame#frame{background-color: rgb(12, 12, 12);\n"
                                 "border-radius:13px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1521, 51))
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color: rgb(51, 51, 51);   border-top-right-radius: 13px;   border-top-left-radius: 13px;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(20, 10, 331, 41))
        self.widget_2.setStyleSheet("QWidget#widget_2{background-color: rgb(12, 12, 12);\n"
                                    " border-top-right-radius: 13px;   border-top-left-radius: 13px;}")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 5, 101, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 11pt \"黑体\";")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 0, 31, 41))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{border-top-right-radius: 0px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 75 20pt \"Segoe UI\";\n"
                                        "}\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(1470, 0, 51, 51))
        self.pushButton.setStyleSheet("QPushButton#pushButton{border-top-right-radius: 13px;\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    font: 75 20pt \"Segoe UI\";\n"
                                      "}\n"
                                      "QPushButton#pushButton:hover{background-color: rgb(255, 42, 0);}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        # self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_2.setGeometry(QtCore.QRect(1420, 0, 51, 51))
        # self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{border-top-right-radius: 0px;\n"
        #                                 "    color: rgb(255, 255, 255);\n"
        #                                 "    font: 75 20pt \"Segoe UI\";\n"
        #                                 "}\n"
        #                                 "QPushButton#pushButton_2:hover{background-color: rgb(116, 116, 116);}\n"
        #                                 "")
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_3.setGeometry(QtCore.QRect(1370, 0, 51, 51))
        # self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{border-top-right-radius: 0px;\n"
        #                                 "    color: rgb(255, 255, 255);\n"
        #                                 "    font: 75 20pt \"Segoe UI\";\n"
        #                                 "}\n"
        #                                 "QPushButton#pushButton_3:hover{background-color: rgb(116, 116, 116);}\n"
        #                                 "")
        # self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 10, 41, 41))
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{border-top-right-radius: 0px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 75 20pt \"Segoe UI\";\n"
                                        "}\n"
                                        "QPushButton#pushButton_5:hover{background-color: rgb(116, 116, 116);}\n"
                                        "")
        self.pushButton_5.setObjectName("pushButton_5")

     # 初始提示符

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_4.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "命令提示符"))
        self.pushButton_4.setText(_translate("MainWindow", "×"))
        self.pushButton.setText(_translate("MainWindow", "×"))
        # self.pushButton_2.setText(_translate("MainWindow", "▢"))
        # self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_5.setText(_translate("MainWindow", "+"))
