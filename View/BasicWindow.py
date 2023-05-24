from PySide6.QtWidgets import QWidget, QMainWindow, QWidget, QVBoxLayout
from View.BasicLayout import ApplicationLayout

class AppMainWindow(QMainWindow):
    MAIN_WINDOW_TITLE = 'Flashcards'
    def __init__(self, flashcards):
        super().__init__()
        self.setWindowTitle(self.MAIN_WINDOW_TITLE)
        self.widget = QWidget()
        self.widget.setLayout(ApplicationLayout(flashcards))
        self.setCentralWidget(self.widget)