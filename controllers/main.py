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
            lambda: self.next_page(self.ui.main)
        )
        self.pages = {
            "main": self.main_widget(),
            "load_browser": self.load_browser_widget(),
            "load_qr": self.load_qr_widget(),
            "main_run": self.main_run(),
            "finish": self.finish(),
            "error": self.error()
        }

        center_window(self)

    def main_widget(self):
        logger.info("main widget loading")
        self.ui.start_main_button.clicked.connect(
            lambda: self.next_page(self.ui.load_browser)
        )

    def load_browser_widget(self):
        logger.info("main widget loading")

    def load_qr_widget(self):
        logger.info("load qr widget loading")
        self.ui.start_qr_button.clicked.connect(
            lambda: self.next_page(self.ui.load_browser)
        )

    def main_run(self):
        logger.info("main run widget loading")

    def finish(self):
        logger.info("finish widget loading")

    def error(self):
        logger.info("error widget loading")

    def next_page(self, next_page: QWidget):
        logger.info(f"Abriendo la pestaña {next_page.objectName()}")
        self.pages[next_page.objectName()]
        self.ui.stackedWidget.setCurrentWidget(next_page)
