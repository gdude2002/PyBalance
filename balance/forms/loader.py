import os.path
import pathlib
from PySide2.QtCore import QFile
from PySide2.QtGui import QWindow

from PySide2.QtUiTools import QUiLoader


class UILoader:
    def __init__(self):
        self.path = pathlib.Path(os.path.dirname(__file__))
        self.loader = QUiLoader()

    def load(self, form: str) -> QWindow:
        ui_path = str(self.path / f"{form}.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)

        return self.loader.load(ui_file)
