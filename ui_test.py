import sys, os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
# from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow, QApplication, QMdiArea, QMdiSubWindow, QPushButton, QGridLayout, QWidget, QProgressBar, QLabel
from pyautogui import size
from qt_material import apply_stylesheet, list_themes
import uimain
import browser
import datetime as dt
# from QtTheme import a

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uimain.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.youtube_btn.clicked.connect(self.open_youtube)
        self.timer = QTimer()
        self.timer.setParent(self)
        self.timer.timeout.connect(self.check_fullscreen)
        self.timer.start(1)
        self.brW = browser.MainWindow()
        
        self.quitapp = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.quitapp.activated.connect(self.quitapps)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.CustomizeWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.Tool, True)

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

    def open_youtube(self):
        self.showMaximized()
        self.activateWindow()
        self.brW.showFullScreen()
        self.setCentralWidget(self.brW)
        self.showFullScreen()

        # options = Options()
        # options.add_experimental_option('detach', True)
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
        #                         options=options)

        # driver.get("https://www.youtube.com/")
        # driver.fullscreen_window()
        # os.system(r"python D:\backu\Kids Mode\selnium_yt.py")


    def check_fullscreen(self):
        current_time = dt.datetime.now().strftime('%H:%M:%S\n%d:%M:%Y')
        try:
            self.ui.time_label.setText(current_time)
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