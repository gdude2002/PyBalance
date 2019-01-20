import os.path
import pathlib

from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QWidget

from balance.forms.stubs.edit_account import EditAccountDialogStub
from balance.forms.stubs.main_window import MainWindowStub


class UILoader:
    """
    Provides a simple wrapper around Qt's .ui file loader, which takes the
    name of a ui file and loads it.
    """
    path = pathlib.Path(os.path.dirname(__file__))
    loader = QUiLoader()

    @classmethod
    def load(cls, form: str) -> QWidget:
        """
        Load up a .ui file and return it.

        :param form: The name of the .ui file to load, without the .ui extension
        :return: The QWidget created from the UI file
        """

        ui_path = str(cls.path / f"forms/designer/{form}.ui")
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)

        return cls.loader.load(ui_file)


main_window: MainWindowStub = UILoader.load("main_window")


def get_edit_account_dialog() -> EditAccountDialogStub:
    return UILoader.load("edit_account")
