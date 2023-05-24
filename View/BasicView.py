from PySide6.QtWidgets import QApplication
from View.BasicWindow import AppMainWindow
import sys

class StartView:
    def __init__(self, flashcards):
        self.app = QApplication(sys.argv)
        self.window = AppMainWindow(flashcards)
    
    def show(self):
        self.window.show()
        sys.exit(self.app.exec())
