import time

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QRadioButton, QGroupBox,
                               QGridLayout, QCheckBox, QHeaderView, QTableWidgetItem, QMessageBox)

from models.FileUpload import FileExcel
from models.Whatsapp import WhatsApp
from utils import center_window, logger
from views.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, db: FileExcel) -> None:
        """Ventana principal
        Args:
            db(FileExcel): Archivo excel donde se encuentra la información
        """
        super(MainWindow, self).__init__()
        # Propiedades
        self.db = db
        self.value_headers = dict()
        self.message = None
        self.phones_header = None
        self.driver = WhatsApp()

        # Iniciando la ventana
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.select_column)
        self.select_column()
        logger.debug("Ejecutando")

        center_window(self)

    def select_column(self):
        """Pestaña para seleccionar las columnas del archivo excel"""
        box_select_numbers = QGroupBox()
        box_select_header = QGroupBox()
        grid_box_numbers = QGridLayout()
        grid_box_headers = QGridLayout()
        col = 0
        radio_button_style = """
            QRadioButton {
              font-size: 14px;
              color: white;
            }
            QRadioButton::indicator {
              width: 14px;
              height: 14px;
            }
            QRadioButton::indicator:hover {
              background-color: #8696a0;
            }
            QRadioButton::indicator:checked {
              width: 6px;
              height: 6px;
              border: 5px solid #38b54a;
              border-radius: 8px;
              background-color: rgba(0, 0, 0, 0);
            }
            QRadioButton::indicator:unchecked {
              border: 1px solid #cccccc;
              border-radius: 8px;
            }
        """
        check_box_style = """
            QCheckBox {
              font-size: 14px;
              color: white;
            }
            QCheckBox::indicator:hover {
              background-color: #8696a0;
            }
            QCheckBox::indicator:checked {
              image: url("./assets/icons/main/check.png");
            }
            QCheckBox::indicator:unchecked {
              border: 1px solid #cccccc;
            }
        """
        for header in self.db.columns.items():
            #: header[0] valor de la celda
            radio_button = QRadioButton(header[0], box_select_numbers)
            checked_button = QCheckBox(header[0], box_select_header)

            #: Añadiendo estilos
            radio_button.setStyleSheet(radio_button_style)
            checked_button.setStyleSheet(check_box_style)
            #: header[1] posición en donde está la celda
            grid_box_numbers.addWidget(radio_button, (header[1] - 1) % 4, col)
            grid_box_headers.addWidget(checked_button, (header[1] - 1) % 4, col)
            col = col + 1 if header[1] % 4 == 0 else col
        box_select_numbers.setLayout(grid_box_numbers)
        box_select_header.setLayout(grid_box_headers)
        self.ui.select_number.addWidget(box_select_numbers, 0, 0)
        self.ui.select_columns.addWidget(box_select_header, 0, 0)
        self.ui.start_button_3.clicked.connect(
            lambda: self.box_verification(
                box_select_numbers, box_select_header)
        )

    def box_verification(self, box1: QGroupBox, box2: QGroupBox):
        """Caja de botones que iran en la pestaña para seleccionar columnas"""
        logger.info("Verificación de las opciones seleccionadas")
        column_number = None
        for button in box1.findChildren(QRadioButton):
            if button.isChecked():
                column_number = button.text()
                break
        column_headers = list()
        for button in box2.findChildren(QCheckBox):
            if button.isChecked():
                column_headers.append(button.text())

        if column_number and column_headers:
            for i in column_headers:
                values = self.db.get_values(i)
                self.phones_header = column_number
                self.value_headers.update({i: values})
            self.main_widget()
        else:
            logger.info("No se ha seleccionado los botones")
            # Definiendo el QMessageBox
            dlg = QMessageBox(self.ui.select_column)
            dlg.setWindowTitle("Seleccionar columnas")
            dlg.setText("Se tiene que seleccionar las opciones")
            dlg.setIcon(QMessageBox.Warning)
            dlg.exec()

    def main_widget(self):
        """Pestaña principal"""
        logger.info("main widget loading")
        logger.debug(f"Columnas: {self.value_headers.keys()}")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)

        # Configurando las opciones de la tabla
        headers = self.value_headers.keys()
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        row_count = self.db.ws.max_row - 1
        self.ui.tableWidget.setRowCount(row_count)

        # Agregando los valores a las celdas de la tabla
        for col, columns in enumerate(self.value_headers.values()):
            for row, value in enumerate(columns):
                if isinstance(value, (float, int)):
                    value = int(value)
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, col, item)

        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Obteniendo el texto del QTextEdit
        self.ui.start_main_button.clicked.connect(
            self.get_message
        )

    def get_message(self):
        """Obtiene le mensaje del QTextEdit para poder enviar."""
        message = self.ui.message_text.toPlainText()
        logger.info(message)
        logger.info(f"Mensaje: {message}")
        if message.replace(" ", ""):
            self.message = message
            self.load_browser_widget()
        else:
            # Mensaje de diálogo, si es que no se mandara un texto vació
            dlg = QMessageBox(self.ui.main)
            dlg.setWindowTitle("Error")
            dlg.setText("¡No se ha colocado el mensaje a enviar!")
            dlg.setIcon(QMessageBox.Warning)
            dlg.exec()

    def load_browser_widget(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.load_qr)
        logger.info("load browser widget loading")
        self.driver.get_driver()
        time.sleep(5)
        self.load_qr_widget()

    def load_qr_widget(self):
        logger.info("load qr widget loading")
        self.ui.stackedWidget.setCurrentWidget(self.ui.load_qr)
        self.ui.start_qr_button.clicked.connect(self.main_run)

    def main_run(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_run)
        self.driver.send_message(
            phones=self.value_headers[self.phones_header],
            message=self.message
        )
        logger.info("main run widget loading")

    def finish(self):
        logger.info("finish widget loading")

    def error(self):
        logger.info("error widget loading")
