# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 0, 951, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_ConnectToRobot = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_ConnectToRobot.setObjectName("pushButton_ConnectToRobot")
        self.horizontalLayout_3.addWidget(self.pushButton_ConnectToRobot)
        self.pushButton_Rviz2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_Rviz2.setObjectName("pushButton_Rviz2")
        self.horizontalLayout_3.addWidget(self.pushButton_Rviz2)
        self.pushButton_Record = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_Record.setObjectName("pushButton_Record")
        self.horizontalLayout_3.addWidget(self.pushButton_Record)
        self.pushButton_RQt = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_RQt.setObjectName("pushButton_RQt")
        self.horizontalLayout_3.addWidget(self.pushButton_RQt)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 951, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Autonomous = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Autonomous.setObjectName("pushButton_Autonomous")
        self.horizontalLayout.addWidget(self.pushButton_Autonomous)
        self.pushButton_ManualControl = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_ManualControl.setObjectName("pushButton_ManualControl")
        self.horizontalLayout.addWidget(self.pushButton_ManualControl)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 330, 741, 121))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_STOP_Nav = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_STOP_Nav.setGeometry(QtCore.QRect(770, 550, 191, 71))
        self.pushButton_STOP_Nav.setObjectName("pushButton_STOP_Nav")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(770, 389, 191, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_StartStopRecord = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_StartStopRecord.setGeometry(QtCore.QRect(770, 450, 191, 41))
        self.pushButton_StartStopRecord.setObjectName("pushButton_StartStopRecord")
        self.pushButton_StartStopRecord_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_StartStopRecord_2.setGeometry(QtCore.QRect(770, 450, 191, 41))
        self.pushButton_StartStopRecord_2.setObjectName("pushButton_StartStopRecord_2")
        self.pushButton_SaveMap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SaveMap.setGeometry(QtCore.QRect(770, 450, 191, 41))
        self.pushButton_SaveMap.setObjectName("pushButton_SaveMap")
        self.pushButton_Emergency = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Emergency.setGeometry(QtCore.QRect(80, 530, 211, 91))
        self.pushButton_Emergency.setObjectName("pushButton_Emergency")
        self.pushButton_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(330, 560, 161, 61))
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 380, 701, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(500, 130, 471, 76))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_JoyControl = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_JoyControl.setObjectName("pushButton_JoyControl")
        self.horizontalLayout_4.addWidget(self.pushButton_JoyControl)
        self.pushButton_KeyboardControl = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_KeyboardControl.setObjectName("pushButton_KeyboardControl")
        self.horizontalLayout_4.addWidget(self.pushButton_KeyboardControl)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 130, 471, 78))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_NewMap = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_NewMap.setObjectName("pushButton_NewMap")
        self.horizontalLayout_2.addWidget(self.pushButton_NewMap)
        self.pushButton_withMap = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_withMap.setObjectName("pushButton_withMap")
        self.horizontalLayout_2.addWidget(self.pushButton_withMap)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "P3DX Robot GUI"))
        self.pushButton_ConnectToRobot.setText(_translate("MainWindow", "Connect to ROBOT"))
        self.pushButton_Rviz2.setText(_translate("MainWindow", "Rviz2"))
        self.pushButton_Record.setText(_translate("MainWindow", "Record  Bag File"))
        self.pushButton_RQt.setText(_translate("MainWindow", "RQt"))
        self.pushButton_Autonomous.setText(_translate("MainWindow", "Autonomous"))
        self.pushButton_ManualControl.setText(_translate("MainWindow", "Manual Control"))
        self.label.setText(_translate("MainWindow", "P3DX Robot GUI"))
        self.pushButton_STOP_Nav.setText(_translate("MainWindow", "Stop Navigation"))
        self.pushButton_StartStopRecord.setText(_translate("MainWindow", "Strart Recording"))
        self.pushButton_StartStopRecord_2.setText(_translate("MainWindow", "Stop Recording"))
        self.pushButton_SaveMap.setText(_translate("MainWindow", "Save Map"))
        self.pushButton_Emergency.setText(_translate("MainWindow", "EMERGENCY"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_JoyControl.setText(_translate("MainWindow", "Joy Stick Contro"))
        self.pushButton_KeyboardControl.setText(_translate("MainWindow", "Keyboard control"))
        self.pushButton_NewMap.setText(_translate("MainWindow", "New Map"))
        self.pushButton_withMap.setText(_translate("MainWindow", "Select Map"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
