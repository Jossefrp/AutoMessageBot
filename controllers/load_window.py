from PySide6.QtWidgets import QMainWindow
from views.ui_load import Ui_LoadWindow
from utils import center_window

class LoadWindow(QMainWindow):
    def __init__(self) -> None:
        super(LoadWindow, self).__init__()
        self.ui = Ui_LoadWindow()
        self.ui.setupUi(self)
        center_window(self)
