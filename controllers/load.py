from PySide6.QtWidgets import QMainWindow, QFileDialog
from views.ui_load import Ui_LoadWindow
from utils import center_window, logger


class LoadWindow(QMainWindow):
    def __init__(self) -> None:
        super(LoadWindow, self).__init__()
        self.ui = Ui_LoadWindow()
        self.ui.setupUi(self)
        center_window(self)

        # Conectando las señales
        self.ui.pushButton.clicked.connect(self.load_file)

    def load_file(self):
        logger.info("Abriendo archivo")
        file_name, _ = QFileDialog.getOpenFileName(
            self.ui.pushButton, "Abrir archivo", "/home", "Excel (*.xlsx *.xlt *.xltx *.xls)"
        )
        if file_name:
            logger.debug(file_name)
        else:
            logger.info("No se ha cargado un archivo") 

    def next_page(self):
        pass