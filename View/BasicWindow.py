from PySide6.QtWidgets import QWidget, QMainWindow, QWidget
from View.BasicLayout import ApplicationLayout

class AppMainWindow(QMainWindow):
    MAIN_WINDOW_TITLE = 'Flashcards'
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.MAIN_WINDOW_TITLE)
        self.widget = QWidget()
        self.widget.setLayout(ApplicationLayout())
        self.setCentralWidget(self.widget)