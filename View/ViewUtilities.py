def set_widget_font_size(widget, font_size):
    font = widget.font()
    font.setPointSize(font_size)
    widget.setFont(font)