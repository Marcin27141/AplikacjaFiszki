import sys
from PySide6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, Signal

class TimerWidget(QWidget):
    TIMEOUT_SIGNAL = Signal()

    def __init__(self, duration):
        super().__init__()

        self.duration = duration
        self.remaining_tenths_of_second = duration * 10

        self.timer_label = QLabel()
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.update_timer_label()

        layout = QVBoxLayout()
        layout.addWidget(self.timer_label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.timeout.connect(self.check_timeout)

    def start(self):
        self.timer.start(100)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.remaining_tenths_of_second = self.duration * 10
        self.update_timer_label()

    def update_timer_label(self):
        seconds = (self.remaining_tenths_of_second % 600) // 10
        tenths = self.remaining_tenths_of_second % 10

        self.timer_label.setText(f"{seconds}.{tenths}")

    def update_timer(self):
        self.remaining_tenths_of_second -= 1
        self.update_timer_label()
        self.check_timeout()

    def check_timeout(self):
        if self.remaining_tenths_of_second <= 0:
            self.timer.stop()
            self.timer_label.setText("Time's up!")
            self.TIMEOUT_SIGNAL.emit()