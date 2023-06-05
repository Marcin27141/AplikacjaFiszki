from PySide6.QtWidgets import QApplication
from View.BasicWindow import AppMainWindow
import sys

class StartView:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = AppMainWindow()
    
    def show(self):
        self.window.show()
        sys.exit(self.app.exec())
