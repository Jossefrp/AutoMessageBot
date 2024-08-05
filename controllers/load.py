from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from controllers.main import MainWindow
from models.file_upload import FileExcel
from utils import center_window, logger
from views.ui_load import Ui_LoadWindow


class LoadWindow(QMainWindow):
    def __init__(self) -> None:
        super(LoadWindow, self).__init__()
        self.main_window = None
        self.ui = Ui_LoadWindow()
        self.ui.setupUi(self)
        self.db = None
        center_window(self)

        # Conectando las señales
        self.ui.pushButton.clicked.connect(self.load_file)

    def load_file(self):
        """Ventana de carga de un archivo"""
        logger.info("Abriendo archivo")
        file_name, _ = QFileDialog.getOpenFileName(
            self.ui.pushButton, "Abrir archivo", "/home", "Excel (*.xlsx *.xlt *.xltx *.xls)"
        )
        if file_name:
            logger.debug(file_name)
            self.load_file_excel(file_name)
            if self.db:
                self.next_page()
        else:
            logger.info("No se ha cargado un archivo")

    def load_file_excel(self, file_name: str) -> None:
        """Verifica si es que hay algún error en la carga del archivo excel"""
        db = FileExcel(file_name)
        if db.error:
            msg = QMessageBox(self.ui.centralwidget)
            msg.setWindowTitle("Error")
            msg.setText(db.error)
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            return

        self.db = db

    def next_page(self):
        """Siguiente página
        Args:

        """
        logger.info("Abriendo la ventana principal")
        self.main_window = MainWindow(self.db)
        self.main_window.show()
        self.hide()
