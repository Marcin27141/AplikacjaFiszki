from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from View.ViewUtilities import set_widget_font_size
from View.BasicTester.BasicIncorrectWidget import BasicIncorrectWidget

class StatsIncorrectWidget(BasicIncorrectWidget):
    def __init__(self, controller):
        super().__init__(controller)