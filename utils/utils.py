from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget


def center_window(window: QWidget) -> None:
    primary_screen = QGuiApplication.primaryScreen().geometry()
    window_geometry = window.frameGeometry()
    window_geometry.moveCenter(primary_screen.center())
    window.move(window_geometry.topLeft())
