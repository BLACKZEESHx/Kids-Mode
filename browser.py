# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import keyboard
import sys
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from PyQt6.QtCore import *
# from PyQt6.QtCore import QScopedPointer
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from PyQt6.QtWidgets import *
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from PyQt6.QtWebEngineWidgets import QWebEngineView
# from PyQt6.QtWebEngineCore import QWebEngineFullScreenRequest
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from PyQt6.QtGui import *
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# from ui_splash_screen import Ui_SplashScreen
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from PyQt6 import QtCore
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from qt_material import *
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
counter = 0
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setStyleSheet('''*{
                                        background:#121019;
                                    }
                                    QTabBar::tab {
                                        border-bottom: none;
                                        padding: 1px 3px;
                                        margin-left: 3px;
                                        width: 80px;
                                        color: #a4a4a4;
                                        height: 20px;
                                        border-top-left-radius:9px;
                                        margin-bottom: 0px;

                                        }
                                    QTabBar::tab:text {
                                        margin-left: 2px;

                                        }
                                    QTabBar::tab:hover{
                                        background: #450d1d;
                                        color: #a4a4a4;

                                        }
                                    QTabBar::tab:selected {
                                        background-color: #121019;
                                        border: 1px solid #fa1e4e;
                                        border-bottom-style: none;
                                        margin-bottom: 0px;
                                        border-left-color: #fa1e4e;
                                        color: white;

                                        }
                                    QTabBar::close-button {
                                        image: url(C:/Users/Black/close.png);
                                        subcontrol-position: right;
                                        }
                                    QTabBar::close-button:hover {
                                        border: 1px solid #2b3548;
                                        }
                                     ''')  # 181b28; border-top-left-radius: 4px; # border-top-right-radius: 4px; border-bottom-color: #fa1e4e;

        # margin-bottom: 1px;
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        apply_stylesheet(self, theme="dark_amber.xml")
        # self.addtab = QWidget(self)
        # self.addtab.mouseDoubleClickEvent(QMouseEvent.buttons(Qt.MouseButton("left")))
        # self.tabs.setCornerWidget(self.addtab)
        # self.tabs.setTabShape(QTabWidget.TabShape("Triangular"))

        # self.tabs.setOverrideCursor(Qt.CursorShape.IBeamCursor)
        # self.tabs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # self.tabs.showEvent(QShowEvent("tab"))
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.tabs.setMovable(True)
        # self.tabs.setTabBarAutoHide(True)
        self.tabs.setToolTip("Double Click On This👆")
        # self.tabs.setTabPosition(QTabWidget.West)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.setCentralWidget(self.tabs)

        close_shortcut = QShortcut(QKeySequence("Ctrl+W"), self.tabs)
        close_shortcut.activated.connect(self.close_current_tab)

        navtb = QToolBar("Navigation")
        navtb.setToolTip('tools ⚙')
        self.tabs.setStatusTip("Do You Want To Open New Tab? press ''ctrl+t")
        
        navtb.setMovable(False)
        
        self.addToolBar(navtb)

        self.tabbtn = QShortcut("ctrl+t", self)
        self.tabbtn.activated.connect(self.new_tab)

        # self.timer = QTimer()
        # self.timer.setParent(self)
        # self.timer.timeout.connect(self.check_fullscreen)
        # self.timer.start(100)
        back_btn = QAction(
            QIcon('leftarrow.png'), "Go Back (alt+ ← arrow)", self)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        back_btn.setToolTip("Go Back (alt+ ← arrow)")

        back_btn.setStatusTip(
            "Do You Want To Go Back?  press 'alt+left arrow'")
        back_btn.setShortcut("alt+left")
        navtb.addAction(back_btn)

        forward_btn = QAction(QIcon(
            'C:\\MacKloud\\resources\\rightarrow.png'), "Go Forward (alt+ → arrow)", self)
        forward_btn.triggered.connect(
            lambda: self.tabs.currentWidget().forward())
        forward_btn.setToolTip("Go Forward (alt+ → arrow)")
        forward_btn.setStatusTip(
            "Do You Want To Go Forward?  press 'alt+right arrow'")
        forward_btn.setShortcut("alt+right")
        navtb.addAction(forward_btn)
        # self.tabs.addAction(forward_btn)

        reload_btn = QAction(QIcon('circular-arrow.png'), '🔄', self)
        reload_btn.triggered.connect(
            lambda: self.tabs.currentWidget().reload())
        # print(self.tabs.currentWidget().reload())
        # ss = QWebEngineHistory().count()
        # print(ss)
        reload_btn.setToolTip("Reload (ctrl+ ֎ r)")
        reload_btn.setStatusTip("Do You Want To Reload?  press 'ctrl+r'")
        reload_btn.setShortcut("ctrl+r")
        navtb.addAction(reload_btn)

        navtb.addSeparator()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.url_bar.setStyleSheet("""
                                *{
                                    margin-top: 3px;
                                    color: white;
                                    font:bold;
                                    height: 30px;
                                    border-style: solid;
                                    background-color:#121019;
                                    border-radius:4px;
                                    selection-background-color: #fa1e4e;
                                }
                                *:hover{
                                    background-color:#4c1326;
                                    border-color:#00dfff;
                                    
                                }
                                *:focus{
                                    background-color: #251f33;
                                }
                                QLineEdit QMenu{
                                    color:white;
                                    font:bold;
                                    height: 180px;
                                    background: #1c1726;
                                }
                                QLineEdit QMenu::item:selected{
                                    background:#8b1b3a;
                                }""")

        navtb.addWidget(self.url_bar)
        stop_btn = QAction('🛑', self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        self.add_new_tab(QUrl('https://www.bing.com/'), 'homepage')
        # self.show()

        self.setWindowTitle('MacKloud')
        self.setWindowIcon(QIcon("icon2.png"))
        # self.setStyleSheet("background: #121019;color:white")  # 161219
        self.setToolTip("Browser🌐")

        # self.setWindowOpacity(0.96)
        self.screen()
        self.nav = navtb
        shortcut1 = QShortcut(QKeySequence("Meta"), self)  # Left Windows key
        shortcut1.setContext(Qt.ShortcutContext.ApplicationShortcut)
        shortcut1.activated.connect(self.block_windows_key)
        
        # shortcut2 = QShortcut(QKeySequence("Meta"), self)  # Right Windows key
        # shortcut2.setContext(Qt.ShortcutContext.ApplicationShortcut)
        # shortcut2.activated.connect(self.block_windows_key)
        # self.tabs.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tabs.customContextMenuRequested.connect(self.contextMenuEvent)

    # def tabremoved(self,i):
    #     self.tabs.setTabIcon(i,QIcon("C:\\MacKloud\\resources\\rightarrow.png"))
        # self.tabs.setTabIcon(i,QIcon("C:\\MacKloud\\resources\\rightarrow.png"))
#
    def show_tab_menu(self, pos):
        self.tab_menu.exec_(self.tabs.mapToGlobal(pos))

    def add_new_tab(self, qurl=None, label="New tab"):
        if qurl is None:
            qurl = QUrl('https://www.bing.com/')

        browser = QWebEngineView() 
        # browser.setContextMenuPolicy(self.browser_menu.contextMenuPolicy())
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        # self.tabs.setTabToolTip(1, browser.page().title)

        browser.urlChanged.connect(
            lambda qurl, browser=browser: self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(
            lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()[0:10]))

    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self):
        if self.tabs.count() > 1:
            current_index = self.tabs.currentIndex()
            self.tabs.removeTab(current_index)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return

        # title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - MacKloud" %
                            self.tabs.currentWidget().page().title())

    def new_tab(self):
        self.add_new_tab()
        # sleep(0.25)
        # playsound('C:/Users/BAREERA/Downloads/newtab.wav')

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        search = self.url_bar.text().replace(" ", "+")

        if (q.scheme() == ""):
            q.setScheme("http")
        if (self.url_bar.text().startswith("youtube.com ")):
            q = QUrl(
                f"https://www.youtube.com/results?search_query={search[12::]}")

        elif (self.url_bar.text().startswith("google.com ")):
            q = QUrl(f"https://www.google.com/search?q={search[11::]}")

        elif not any([self.url_bar.text().startswith("www."), self.url_bar.text().endswith(".com")]):
            q = QUrl(f"https://www.bing.com/search?q={search[0::]}")

        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return

        self.url_bar.setText(q.toString())
        if self.url_bar.text() == "https://www.bing.com/":
            self.url_bar.setText("")

        self.url_bar.setCursorPosition(0)

    # def check_fullscreen(self):
    #     if self.isFullScreen() is False:
    #         self.showFullScreen()

    #     else:
    #         pass


    def block_windows_key(self):
        print("sd")  # Add your desired actions or leave it empty to block the key press event
            # QMessageBox.information(self, "No Closed Tabs", "There are no closed tabs to reopen.")


# def abb():
#     app = QApplication(sys.argv)
#     win = QWidget()
#     # QApplication.setWindowIcon(QIcon("D:/alldownloadafterdownload/macklogo.png"))
#     win.setToolTip("Browser")
#     window = MainWindow()
#     sys.exit(app.exec_())
# abb()
# SPLASH SCREEN

# class SplashScreen(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_SplashScreen()
#         self.ui.setupUi(self)

#         ## UI ==> INTERFACE CODES
#         ########################################################################

#         ## REMOVE TITLE BAR
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)


#         ## DROP SHADOW EFFECT
#         self.shadow = QGraphicsDropShadowEffect(self)
#         self.shadow.setBlurRadius(20)
#         self.shadow.setXOffset(0)
#         self.shadow.setYOffset(0)
#         self.shadow.setColor(QColor(0, 0, 0, 60))
#         self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

#         ## QTIMER ==> START
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.progress)
#         # TIMER IN MILLISECONDS
#         self.timer.start(35)

#         # CHANGE DESCRIPTION

#         # Initial Text
#         self.ui.label_description.setText("<strong>WELCOME</strong> TO BROWSER")

#         # Change Texts
#         QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
#         QTimer.singleShot(2300, lambda: self.ui.label_description.setText("<strong>LOADING...</strong>"))
#         QTimer.singleShot(2500, lambda: self.ui.label_description.setText("<strong>LOADING..</strong>"))
#         QTimer.singleShot(2800, lambda: self.ui.label_description.setText("<strong>LOADING.</strong>"))
#         QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong>"))
#         QTimer.singleShot(3500, lambda: self.ui.label_description.setText("<strong>LOADING.</strong>"))
#         QTimer.singleShot(3800, lambda: self.ui.label_description.setText("<strong>LOADING..</strong>"))
#         QTimer.singleShot(4000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


#         ## SHOW ==> MAIN WINDOW
#         ########################################################################
#         self.show()
#         ## ==> END ##

#     ## ==> APP FUNCTIONS
#     ########################################################################
#     def progress(self):

#         global counter

#         # SET VALUE TO PROGRESS BAR
#         self.ui.progressBar.setValue(counter)

#         # CLOSE SPLASH SCREE AND OPEN APP
#         if counter > 100:
#             # STOP TIMER
#             self.timer.stop()

#             # SHOW MAIN WINDOW
#             self.main = MainWindow()
#             self.main.show()

#             # CLOSE SPLASH SCREEN
#             self.close()

#         # INCREASE COUNTER
#         counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
