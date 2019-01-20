from PySide2.QtWidgets import QDialog, QFormLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton


class EditAccountDialogStub(QDialog):
    form_layout: QFormLayout
    horizontal_layout: QHBoxLayout

    account_name_input: QLineEdit
    account_name_label: QLabel

    initial_balance_input: QLineEdit
    initial_balance_label: QLabel

    balance_view: QLabel
    balance_label: QLabel

    cancel_button: QPushButton
    ok_button: QPushButton
    recalculate_button: QPushButton
