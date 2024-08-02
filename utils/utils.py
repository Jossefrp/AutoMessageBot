import webbrowser

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget

from utils.logging_config import logger


def center_window(window: QWidget) -> None:
    """Centra la ventana
    Args:
        window: Una ventana QWidget
    Returns:
        None
    """
    primary_screen = QGuiApplication.primaryScreen().geometry()
    window_geometry = window.frameGeometry()
    window_geometry.moveCenter(primary_screen.center())
    window.move(window_geometry.topLeft())


def open_browser(url: str) -> None:
    """Abre el navegador en una url específica
    Args:
        url: Una url de una página web
    Returns:
        None
    """
    logger.info(f'Abriendo {url}')
    webbrowser.open(url)
