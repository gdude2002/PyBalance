import sys

from PySide2.QtWidgets import QApplication

from balance.ui import UILoader

app = QApplication(sys.argv)
ui_loader = UILoader()

window = ui_loader.load("main_window")
window.show()

sys.exit(app.exec_())
