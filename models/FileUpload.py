import openpyxl

from utils import logger


class FileExcel:

    def __init__(self, file) -> None:
        """Clase que abstrae un documento excel
        Args:
            file(str): Nombre del archivo
        """
        self.error = None

        try:
            self.ws = openpyxl.load_workbook(file).active
        except (FileNotFoundError, PermissionError, openpyxl.utils.exceptions.InvalidFileException) as e:
            if isinstance(e, FileNotFoundError):
                self.error = f"No se encuentra el archivo {file}"
            elif isinstance(e, PermissionError):
                self.error = f"No se tiene permisos para acceder al siguiente archivo: {file}"
            elif isinstance(e, openpyxl.utils.exceptions.InvalidFileException):
                self.error = f"El archivo {file} no es un archivo válido de Excel"
            logger.error(self.error)
        except Exception as e:
            self.error = f"Ocurrió un error inesperado: {e}\nNo se puede abrir el archivo"
            logger.error(self.error)
        else:
            self.columns = dict(self.get_headers())

    def get_headers(self) -> list:
        """Obtiene las columnas del archivo
        Returns:
            Lista de las columnas del archivo
        """
        columns = [
            (self.ws.cell(row=1, column=i).value, i) for i in range(1, self.ws.max_column + 1)
        ]
        return columns

    def get_values(self, header: str) -> list:
        """Obtiene los valores de una columna específica
        Args:
            header: Nombre de columna del archivo
        Returns:
            Lista con los valores de una columna específica
        """
        values_columns = [
            self.ws.cell(row=i, column=self.columns[header]).value for i in range(2, self.ws.max_row + 1)
        ]
        return values_columns
