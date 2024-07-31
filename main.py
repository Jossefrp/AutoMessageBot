import sys
from PySide6.QtWidgets import QApplication
from controllers.login import MainWindowForm

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindowForm()
    window.show()

    sys.exit(app.exec())
