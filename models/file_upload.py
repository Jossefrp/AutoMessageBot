import openpyxl
from utils import logger


class FileExcel:
    """Clase que permite incorporar un archivo excel"""

    def __init__(self, file) -> None:
        self.ws = openpyxl.load_workbook(file).active
        self.columns = dict(self.get_headers())

    def get_headers(self) -> list:
        columns = [
            (self.ws.cell(row=1, column=i).value, i) for i in range(1, self.ws.max_column+1)
        ]
        return columns

    def get_values(self, header) -> list:
        values_columns = [
            self.ws.cell(row=i, column=self.columns[header]).value for i in range(2, self.ws.max_row+1)
        ]
        return values_columns
