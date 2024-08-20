import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from controllers.login import MainWindowForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./assets/icons/img_app.ico'))
    window = MainWindowForm()
    window.show()

    sys.exit(app.exec())
