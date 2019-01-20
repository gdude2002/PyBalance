import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication


__all__ = ["app"]

QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # For high density displays
QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # Apparently good practise for some reason

app = QApplication(sys.argv)
