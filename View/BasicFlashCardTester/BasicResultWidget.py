from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from View.ViewUtilities import set_widget_font_size

class BasicResultWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title_label = QLabel("The end")
        self.initialize_title_label()

        self.again_button = QPushButton("Try again")
        self.again_button.clicked.connect(self.retake_the_test)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.title_label)
        widget_layout.addWidget(self.again_button)
        self.setLayout(widget_layout)

    def initialize_title_label(self):
        set_widget_font_size(self.title_label, 20)
        self.title_label.setAlignment(Qt.AlignHCenter)

    def retake_the_test(self):
        self.controller.retake_the_test()