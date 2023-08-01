import ui_testx, sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMdiArea, QMdiSubWindow, QPushButton, QGridLayout, QWidget, QProgressBar, QLabel
from qt_material import apply_stylesheet, list_themes



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui_testx.Ui_MainWindow()
        self.ui.setupUi(self)
        self.subwindow = QMdiSubWindow(self.ui.mdiArea)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme=list_themes()[0])
    window.showFullScreen()
    sys.exit(app.exec())