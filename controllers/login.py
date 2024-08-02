from PySide6.QtWidgets import QMainWindow, QMessageBox

from controllers.load import LoadWindow
from utils import center_window, logger, open_browser
from views.ui_login import Ui_LoginWindow


class MainWindowForm(QMainWindow):
    def __init__(self) -> None:
        super(MainWindowForm, self).__init__()
        self.load_window = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.info_button.clicked.connect(self.info_window)
        self.ui.linkd_button.clicked.connect(
            lambda: open_browser(
                url="https://www.linkedin.com/in/jossef-ramos/")
        )
        self.ui.github_button.clicked.connect(
            lambda: open_browser("https://github.com/Jossefrp")
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

    def next_page(self) -> None:
        logger.info("Abriendo ventana LoadWindow")
        self.load_window = LoadWindow()
        self.load_window.show()
        self.hide()
