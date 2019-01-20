import sys

from balance import app
from balance.forms.impl.main_window import MainWindow


main_window = MainWindow()
main_window.setup()
main_window.show()

sys.exit(app.exec_())
