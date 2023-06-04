from PySide6.QtGui import QFont

def set_widget_font_size(widget, font_size):
    font = widget.font()
    font.setPointSize(font_size)
    widget.setFont(font)

def make_font_bold(widget):
    font = widget.font()
    font.setWeight(QFont.Bold)
    widget.setFont(font)