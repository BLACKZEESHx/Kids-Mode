# Importing Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QMdiArea, QMdiSubWindow, QPushButton, QGridLayout, QWidget, QProgressBar, QLabel, QLineEdit
from qt_material import apply_stylesheet, list_themes
import uimain
import datetime as dt

# Creating class for new application
class MainWindow(QMainWindow):
    # Initialize application
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # variable for ui of main window
        self.ui = uimain.Ui_MainWindow()
        
        # Setting up ui on main window
        self.ui.setupUi(self)
        
        # If youtube button is clicked so open youtube
        self.ui.youtube_btn.clicked.connect(self.open_youtube)
        
        # Like youtube button it works exactly same but just different 
        # is youtube button open youtube and this open setttings app of this application
        self.ui.setting_btn.clicked.connect(self.open_setting)
        
        # Create Timer to check every second function(bla, blaa...)
        self.timer = QTimer()
        self.timer.setParent(self)
        self.timer.timeout.connect(self.check_fullscreen)
        self.timer.start(1)

        # Create button for to all app that opened in this window
        self.quitapp = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.quitapp.activated.connect(self.quitapps)

        # self.ui.time_label.setStyleSheet("border: 5px solid white")
        
        # Setting Window Flags
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.Tool, True)
        
    # function for when setting app is closing so set ui again
    def setting_appcloseEvent(self, event):
        self.ui.setupUi(self)
        self.ui.setting_btn = QPushButton(parent=self.ui.widget)
        self.ui.setting_btn.setMaximumSize(QSize(80, 72))
        self.ui.setting_btn.setStyleSheet("")
        self.ui.setting_btn.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("assets\\settings.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.setting_btn.setIcon(icon1)
        self.ui.setting_btn.setIconSize(QSize(60, 64))
        self.ui.setting_btn.setObjectName("setting_btn")
        self.ui.horizontalLayout.addWidget(self.ui.setting_btn)


    # It's connected to quitapp when quitapp button will be pressed it to close all window other wise it will ignore it
    def quitapps(self):
        try:
            self.brW.close()
        except RuntimeWarning as e:
            pass
        self.showFullScreen()
        self.ui.setupUi(self)
        self.ui.youtube_btn.clicked.connect(self.open_youtube)

    # this conneted to setting button when setting button is clicked so it will open a window inside window
    def open_setting(self):
        self.mdarea = QMdiArea()
        self.subwindow = QMdiSubWindow(self.mdarea)
        self.subwindow.showMaximized()
        self.subwindow.closeEvent = self.setting_appcloseEvent
        self.mdarea.setGeometry(self.subwindow.geometry())
        self.subwindow.setWidget(QLineEdit())

        self.setCentralWidget(self.mdarea)

    # this connected to youtube button when youtube button is clicked it show youtube page
    def open_youtube(self):
        self.showMaximized()
        self.activateWindow()
        # self.brW.showFullScreen()
        # self.setCentralWidget(self.brW)
        self.showFullScreen()


    # this function connects to timer it check every second time and is window is fullscreen
    def check_fullscreen(self):
        current_time = dt.datetime.now().strftime('%H:%M:%S')
        # self.ui.time_label.geometry().setWidth(self.ui.time_label.width()+10)
        try:
            self.ui.time_label.setText(current_time)
            self.ui.time_label.resize(self.ui.time_label.width()+3, self.ui.time_label.height())
        except RuntimeError as e:
            pass
        if self.isFullScreen() is False:
            self.showFullScreen()
        else:
            pass

# Running application
if __name__ == "__main__":

    # create The Application runner
    app = QApplication(sys.argv)
    
    # Create the Application Object
    window = MainWindow()
    
    # Style the Application
    apply_stylesheet(app, theme=list_themes()[0])
    
    # Show the Application
    window.showFullScreen()
    
    # Excute the Application
    sys.exit(app.exec())
    