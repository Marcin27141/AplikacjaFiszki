from PySide6.QtWidgets import QTableWidget, QLineEdit, QLabel, QWidget, QHBoxLayout

class NameWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        name_layout = QHBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_line_edit)
        self.setLayout(name_layout)