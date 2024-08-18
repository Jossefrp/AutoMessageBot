import sys

from PySide6.QtCore import Qt, QThreadPool, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QMainWindow, QRadioButton, QGroupBox,
                               QGridLayout, QCheckBox, QTableWidgetItem, QMessageBox, QTableWidget)

from models.FileUpload import FileExcel, ActiveExcelFile
from models.ObjectApp import ObjectApp
from models.WhatsappWorker import WhatsappWorker, SendMessageWorker
from utils import center_window, logger
from views.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, file_excel: FileExcel) -> None:
        """Ventana principal
        Args:
            db(FileExcel): Archivo excel donde se encuentra la información
        """
        super(MainWindow, self).__init__()
        # Propiedades
        self.send_message = None
        self.file_excel = file_excel
        self.active_file = ActiveExcelFile(file_excel)
        self.message = None
        self.whatsapp = WhatsappWorker()
        self.threadpool = QThreadPool()

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
        for header in self.file_excel.columns.items():
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
        columns_headers = list()
        for button in box2.findChildren(QCheckBox):
            if button.isChecked():
                columns_headers.append(button.text())

        if column_number and columns_headers:
            self.active_file.columns = columns_headers
            self.active_file.column_number = column_number
            self.active_file.get_columns_values()

            logger.info(self.active_file.objects)
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
        logger.debug(f"Columnas: {self.active_file.columns}")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)

        self.generate_table_widget(self.ui.tableWidget)

        # Obteniendo el texto del QTextEdit
        self.ui.start_main_button.clicked.connect(
            self.get_message
        )

    def get_message(self):
        """Obtiene el mensaje del QTextEdit para poder enviar."""
        message = self.ui.message_text.toPlainText()
        logger.info(f"Mensaje: {message}")
        if not message.replace(" ", ""):
            # Mensaje de diálogo, si es que no se mandara un texto vació
            dlg = QMessageBox(self.ui.main)
            dlg.setWindowTitle("Error")
            dlg.setText("¡No se ha colocado el mensaje a enviar!")
            dlg.setIcon(QMessageBox.Warning)
            dlg.exec()

        self.message = message
        self.load_browser_widget()

    def load_browser_widget(self):
        logger.info("load browser widget loading")
        self.ui.stackedWidget.setCurrentWidget(self.ui.load_browser)
        QTimer.singleShot(300, lambda: self.threadpool.start(self.whatsapp))
        if self.whatsapp.error:
            dlg = QMessageBox(self.ui.load_browser)
            dlg.setWindowTitle("Error en el navegador")
            dlg.setText(self.whatsapp.error)
            dlg.setIcon(QMessageBox.Critical)
            dlg.exec()
            if dlg:
                sys.exit(1)
        self.load_qr_widget()

    def load_qr_widget(self):
        logger.info("load qr widget loading")
        QTimer.singleShot(
            8_000,
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.load_qr)
        )
        self.ui.start_qr_button.clicked.connect(self.main_run)

    def main_run(self):
        logger.info("main run widget loading")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_run)
        self.ui.message_text_2.setText(self.message)

        self.generate_table_widget(self.ui.tableWidget_2, "Status")
        phones = [
            object_app.values for object_app in self.active_file.objects if
            object_app.header == self.active_file.column_number
        ][0]

        logger.info(f"Phone values: {phones}")
        self.send_message = SendMessageWorker(self.whatsapp.driver, phones, message=self.message)
        self.send_message.signals.result.connect(self.status_number)
        self.send_message.signals.finished.connect(self.finish)
        self.send_message.signals.progress.connect(self.progress_bar)
        self.threadpool.start(
            self.send_message
        )
        self.ui.stop_button.clicked.connect(lambda: self.send_message.signals.finished.emit())


    def progress_bar(self, row):
        percentage = row / (self.ui.tableWidget_2.rowCount() - 1) * 100
        logger.info(f"Porcentaje: {percentage}")

        if row >= 1:
            for col in range(self.ui.tableWidget_2.columnCount()-1):
                self.ui.tableWidget_2.item(row - 1, col).setBackground(QColor(255, 255, 255))

        for col in range(self.ui.tableWidget_2.columnCount()-1):
            self.ui.tableWidget_2.item(row, col).setBackground(QColor(52, 125, 235))
        self.ui.progressBar.setValue(percentage)


    def status_number(self, data):
        item = QTableWidgetItem(data[1])
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget_2.setItem(data[0], self.ui.tableWidget_2.columnCount() - 1, item)


    def finish(self):
        logger.info("finish widget loading")
        self.active_file.objects = ObjectApp(header="Status", values=self.send_message.status)
        QTimer.singleShot(
            1000,
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.finish)
        )

        self.generate_table_widget(self.ui.tableWidget_3)


    def error(self):
        logger.info("error widget loading")


    def generate_table_widget(self, table: QTableWidget, *args):
        # Configurando las opciones de la tabla
        headers = self.active_file.columns
        if args:
            headers += args
        table.setColumnCount(self.active_file.get_count_columns())
        table.setHorizontalHeaderLabels(headers)
        row_count = self.active_file.get_count_values()
        table.setRowCount(row_count)

        # Agregando los valores a las celdas de la tabla
        logger.info(f"Columnas: {len(self.active_file.objects)}")
        flag = False
        for col, object_app in enumerate(self.active_file.objects):
            if object_app.status is False:
                flag = True
                continue

            col = col - 1 if flag and table is self.ui.tableWidget_3 else col
            for row, value in enumerate(object_app.values):
                if isinstance(value, (float, int)):
                    value = int(value)
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, col, item)
