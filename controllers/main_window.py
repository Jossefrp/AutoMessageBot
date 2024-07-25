from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.ui_login import Ui_LoginWindow
from controllers.load_window import LoadWindow
from utils import center_window
import logging
import webbrowser

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MainWindowForm(QMainWindow):
    def __init__(self) -> None:
        super(MainWindowForm, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.info_button.clicked.connect(self.info_window)
        self.ui.linkd_button.clicked.connect(
            lambda: self.open_browser(
                url="https://www.linkedin.com/in/jossef-ramos/")
        )
        self.ui.github_button.clicked.connect(
            lambda: self.open_browser("https://github.com/Jossefrp")
        )
        self.ui.start_button.clicked.connect(self.next_page)
        center_window(self)

    def info_window(self) -> None:
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Información")
        dlg.setText(
            "Aplicación que manda mensajes de WhatsApp mediante un excel proporcionado."
        )
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()
        if button == QMessageBox.Ok:
            logger.info("Información mostrada")

    def open_browser(self, url: str) -> None:
        logger.info(f"Abriendo el navegador con URL: {url}")
        webbrowser.open_new_tab(url)

    def next_page(self) -> None:
        logger.info("Abriendo ventana LoadWindow")
        self.load_window = LoadWindow()
        self.load_window.show()
        self.hide()
