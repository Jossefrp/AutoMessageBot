from PySide6.QtWidgets import QMainWindow, QWidget
from views.ui_main import Ui_MainWindow
from utils import center_window, logger


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.select_column)
        self.ui.start_button_3.clicked.connect(
            lambda: self.next_page(self.ui.main))
        center_window(self)

    def next_page(self, next_page: QWidget):
        logger.info(f"Abriendo la pestaña {next_page.objectName()}")
        self.ui.stackedWidget.setCurrentWidget(next_page)

    def main_widget(self):
        pass

    def load_browser_widget(self):
        pass

    def load_qr_widget(self):
        pass

    def main_run(self):
        pass

    def finish(self):
        pass

    def error(self):
        pass
