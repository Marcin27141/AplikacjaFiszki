from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from View.ViewUtilities import set_widget_font_size

class BasicResultWidget(QWidget):
    RETURN_TO_MENU = Signal()
    RETAKE_THE_TEST = Signal()

    def __init__(self):
        super().__init__()
        self.title_label = QLabel("The end")
        self.initialize_title_label()

        self.finish_button = QPushButton("Finish")
        self.finish_button.clicked.connect(self.RETURN_TO_MENU.emit)

        self.again_button = QPushButton("Try again")
        self.again_button.clicked.connect(self.RETAKE_THE_TEST.emit)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.title_label)
        widget_layout.addWidget(self.again_button)
        self.setLayout(widget_layout)

    def initialize_title_label(self):
        set_widget_font_size(self.title_label, 20)
        self.title_label.setAlignment(Qt.AlignHCenter)