from PySide6.QtWidgets import QMainWindow, QWidget, QRadioButton, QGroupBox, QGridLayout, QCheckBox
from views.ui_main import Ui_MainWindow
from utils import center_window, logger
from models.file_upload import FileExcel


class MainWindow(QMainWindow):
    def __init__(self, file) -> None:
        super(MainWindow, self).__init__()
        self.file = file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.select_column)
        self.select_column()
        self.pages = {
            "main": lambda: self.main_widget,
            "load_browser": lambda: self.load_browser_widget(),
            "load_qr": lambda: self.load_qr_widget(),
            "main_run": lambda: self.main_run(),
            "finish": lambda: self.finish(),
            "error": lambda: self.error()
        }

        center_window(self)

    def select_column(self):
        db = FileExcel(self.file)
        box_select_numbers = QGroupBox()
        box_select_header = QGroupBox()
        box_select_header.setFlat(True)
        grid_box_numbers = QGridLayout()
        grid_box_headers = QGridLayout()
        col = 0
        for header in db.columns.items():
            radio_button = QRadioButton(header[0], box_select_numbers)
            checked_button = QCheckBox(header[0], box_select_header)
            grid_box_numbers.addWidget(radio_button, (header[1]-1)%3, col)
            grid_box_headers.addWidget(checked_button, (header[1]-1)%3, col)
            col = col + 1 if header[1] %3 == 0 else col
        box_select_numbers.setLayout(grid_box_numbers)
        box_select_header.setLayout(grid_box_headers)
        self.ui.select_number.addWidget(box_select_numbers, 0, 0)
        self.ui.select_columns.addWidget(box_select_header, 0, 0)
        self.ui.start_button_3.clicked.connect(
            lambda: self.box_verification(box_select_numbers, box_select_header)
        )

    def box_verification(self, box1: QGroupBox, box2: QGroupBox):
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
            print(f"Select number: {column_number}")
            print(f"Select headers: {column_headers}")
            self.next_page(self.ui.main)
        else:
            print("No selection")
        

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
