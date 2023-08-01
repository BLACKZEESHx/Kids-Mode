import sys, os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
# from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow, QApplication, QMdiArea, QMdiSubWindow, QPushButton, QGridLayout, QWidget, QProgressBar, QLabel, QLineEdit
from pyautogui import size
from qt_material import apply_stylesheet, list_themes
import uimain
# import browser
import datetime as dt
# from QtTheme import a

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uimain.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.youtube_btn.clicked.connect(self.open_youtube)
        self.ui.setting_btn.clicked.connect(self.open_setting)
        self.timer = QTimer()
        self.timer.setParent(self)
        self.timer.timeout.connect(self.check_fullscreen)
        self.timer.start(1)

        self.quitapp = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.quitapp.activated.connect(self.quitapps)
        # self.ui.time_label.setStyleSheet("border: 5px solid white")
        # self.ui.time_label.geometry().setWidth(self.ui.time_label.width()+8)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.CustomizeWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.Tool, True)
        # self.ui.windowW.setVisible(True)
        
        # QMdiSubWindow

    def setting_appcloseEvent(self, event):
        self.ui.setupUi(self)

    def quitapps(self):
        try:
            self.brW.close()
        except RuntimeWarning as e:
            pass
        self.showFullScreen()
        self.ui.setupUi(self)
        self.ui.youtube_btn.clicked.connect(self.open_youtube)

        # if self.brW.isVisible():
            # self.brW.setVisible(False)
        
        # self.brW.setVisible(True)

    def open_setting(self):
        self.mdarea = QMdiArea()
        self.subwindow = QMdiSubWindow(self.mdarea)
        self.subwindow.showMaximized()
        self.subwindow.closeEvent = self.setting_appcloseEvent
        self.mdarea.setGeometry(self.subwindow.geometry())
        self.subwindow.setWidget(QLineEdit())

        self.setCentralWidget(self.mdarea)

    def open_youtube(self):
        self.showMaximized()
        self.activateWindow()
        # self.brW.showFullScreen()
        # self.setCentralWidget(self.brW)
        self.showFullScreen()

        # options = Options()
        # options.add_experimental_option('detach', True)
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
        #                         options=options)

        # driver.get("https://www.youtube.com/")
        # driver.fullscreen_window()
        # os.system(r"python D:\backu\Kids Mode\selnium_yt.py")


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme=list_themes()[0])
    window.showFullScreen()
    sys.exit(app.exec())