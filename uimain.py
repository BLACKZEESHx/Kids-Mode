# Form implementation generated from reading ui file 'assets\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 822)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.central_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.central_widget.setStyleSheet("")
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.time_bar_widget = QtWidgets.QWidget(parent=self.central_widget)
        self.time_bar_widget.setMinimumSize(QtCore.QSize(0, 200))
        self.time_bar_widget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.time_bar_widget.setObjectName("time_bar_widget")
        self.label = QtWidgets.QLabel(parent=self.time_bar_widget)
        self.label.setGeometry(QtCore.QRect(110, 20, 151, 31))
        self.label.setStyleSheet("*{\n"
"font: 16pt \"Game Of Squids\";\n"
"}")
        self.label.setObjectName("label")
        self.remaining_time_bar = QtWidgets.QProgressBar(parent=self.time_bar_widget)
        self.remaining_time_bar.setGeometry(QtCore.QRect(330, 130, 121, 31))
        self.remaining_time_bar.setStyleSheet("/*  ------------------------------------------------------------------------  */\n"
"/*  QProgressBar  */\n"
"\n"
"QProgressBar {\n"
"  border-radius: 0;\n"
"  background-color: #4f5b62;\n"
"  text-align: center;\n"
"  color: solid black;\n"
"  \n"
"    font: 14pt \"Game Of Squids\";\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #ffd740;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"")
        self.remaining_time_bar.setProperty("value", 24)
        self.remaining_time_bar.setObjectName("remaining_time_bar")
        self.verticalLayout.addWidget(self.time_bar_widget)
        self.widget = QtWidgets.QWidget(parent=self.central_widget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.youtube_btn = QtWidgets.QPushButton(parent=self.widget)
        self.youtube_btn.setMaximumSize(QtCore.QSize(80, 64))
        self.youtube_btn.setStyleSheet("")
        self.youtube_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets\\youtube.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.youtube_btn.setIcon(icon)
        self.youtube_btn.setIconSize(QtCore.QSize(64, 64))
        self.youtube_btn.setObjectName("youtube_btn")
        self.horizontalLayout.addWidget(self.youtube_btn)
        self.setting_btn = QtWidgets.QPushButton(parent=self.widget)
        self.setting_btn.setMaximumSize(QtCore.QSize(80, 72))
        self.setting_btn.setStyleSheet("")
        self.setting_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets\\settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setting_btn.setIcon(icon1)
        self.setting_btn.setIconSize(QtCore.QSize(60, 64))
        self.setting_btn.setObjectName("setting_btn")
        self.horizontalLayout.addWidget(self.setting_btn)
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout.addWidget(self.central_widget, 1, 0, 1, 1)
        self.top_menu = QtWidgets.QWidget(parent=self.centralwidget)
        self.top_menu.setMinimumSize(QtCore.QSize(11, 30))
        self.top_menu.setMaximumSize(QtCore.QSize(16777215, 30))
        self.top_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.top_menu.setObjectName("top_menu")
        self.time_label = QtWidgets.QLabel(parent=self.top_menu)
        self.time_label.setGeometry(QtCore.QRect(690, 10, 47, 16))
        self.time_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.time_label.setObjectName("time_label")
        self.gridLayout.addWidget(self.top_menu, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kids Mode"))
        self.time_label.setText(_translate("MainWindow", "time"))
