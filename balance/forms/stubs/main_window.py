from PySide2.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QTableView,
    QListWidget, QToolBar, QAction, QStatusBar)


class MainWindowStub(QMainWindow):
    # verticalLayout: QVBoxLayout
    # horizontalLayout: QHBoxLayout
    # horizontalSpacer: Spacer

    central_widget: QWidget
    account_switcher: QListWidget
    status_bar: QStatusBar

    left_tool_bar: QToolBar

    action_new_database: QAction
    action_open_database: QAction
    action_new_account: QAction
    action_edit_account: QAction
    action_delete_account: QAction

    right_tool_bar: QToolBar

    action_help: QAction
    action_about: QAction

    balance_label: QLabel
    date_label: QLabel

    button_next_month: QPushButton
    button_previous_month: QPushButton
    button_pick_month: QPushButton

    transactions_table: QTableView
