from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.ui_login import Ui_LoginWindow
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MainWindowForm(QMainWindow):
    def __init__(self) -> None:
        super(MainWindowForm, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.info_button.clicked.connect(self.info_window)

        self.center_window()

    def center_window(self):
        primary_screen = QGuiApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(primary_screen.center())
        self.move(window_geometry.topLeft())

    def info_window(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Información")
        dlg.setText(
            "Aplicación que manda mensajes de WhatsApp mediante un excel proporcionado."
        )
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()
        if button == QMessageBox.Ok:
            logger.info("Información mostrada")

    def view_password(self):
        logger.info("View password")
