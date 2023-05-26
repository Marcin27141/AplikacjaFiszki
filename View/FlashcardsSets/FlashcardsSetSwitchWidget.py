from PySide6.QtWidgets import QTableWidget, QLineEdit, QTableWidgetItem, QHeaderView, QStackedLayout, QWidget
from PySide6.QtCore import Qt
from View.FlashcardsSets.FlashcardsSetEditorWidget import FlashcardsSetEditorWidget
from View.FlashcardsSets.FlashcardsSetListTable import FlashcardsSetListTable

class FlashcardsSetSwitchWidget(QWidget):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.show_sets_widget = FlashcardsSetListTable(self.controller)
        self.edit_sets_widget = FlashcardsSetEditorWidget(self.controller)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.show_sets_widget)
        self.stacked_layout.addWidget(self.edit_sets_widget)
        self.setLayout(self.stacked_layout)