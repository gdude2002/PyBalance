from balance.abc import Window
from balance.forms.stubs.main_window import MainWindowStub
from balance.ui import main_window


class MainWindow(Window):
    def __init__(self):
        self._window: MainWindowStub = main_window

    def setup(self):
        self._window.action_new_database.triggered.connect(self.new_database_clicked)
        self._window.action_open_database.triggered.connect(self.open_database_clicked)
        self._window.action_new_account.triggered.connect(self.new_account_clicked)
        self._window.action_edit_account.triggered.connect(self.edit_account_clicked)
        self._window.action_delete_account.triggered.connect(self.delete_account_clicked)
        self._window.action_help.triggered.connect(self.help_clicked)
        self._window.action_about.triggered.connect(self.about_clicked)

        self._window.button_next_month.clicked.connect(self.next_month_clicked)
        self._window.button_previous_month.clicked.connect(self.previous_month_clicked)
        self._window.button_pick_month.clicked.connect(self.pick_month_clicked)

        self._window.account_switcher.clicked.connect(self.account_switcher_clicked)
        self._window.transactions_table.clicked.connect(self.transactions_table_clicked)

    def show(self):
        self._window.show()

    def new_database_clicked(self):
        print("Clicked: New Database")

    def open_database_clicked(self):
        print("Clicked: Open Database")

    def new_account_clicked(self):
        print("Clicked: New Account")

    def edit_account_clicked(self):
        print("Clicked: Edit Account")

    def delete_account_clicked(self):
        print("Clicked: Delete Account")

    def help_clicked(self):
        print("Clicked: Help")

    def about_clicked(self):
        print("Clicked: About")

    def next_month_clicked(self):
        print("Clicked: Next month")

    def previous_month_clicked(self):
        print("Clicked: Previous Month")

    def pick_month_clicked(self):
        print("Clicked: Pick Month")

    def account_switcher_clicked(self):
        print("Clicked: Account Switcher")

    def transactions_table_clicked(self):
        print("Clicked: Transactions Table")
