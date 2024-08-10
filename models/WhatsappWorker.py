import os
import time

from PySide6.QtCore import QRunnable, Slot, QObject, Signal
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from models.FilterNumbers import FilterNumbers
from utils.logging_config import logger


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    """
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs["progress_callback"] = self.signals.progress

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            pass
        finally:
            self.signals.finished.emit()

class WhatsappWorker(QRunnable):
    """Clase que tiene los métodos para poder trabajar con WhatsappWeb"""

    def __init__(self):
        super(WhatsappWorker, self).__init__()
        self.driver = None
        self.error = None
        self.signals = WorkerSignals()

    def send_message(self, phones, message):
        """Permite el envío de mensajes mediante whatsapp web
        Args:
            phones(list): Lista de números de celular
            message(str): Mensaje que se enviara

        Returns:
            None
        """
        send_message = SendMessageWorker(self.driver, phones, message)
        return send_message

    @Slot()
    def run(self):
        """Nos permite abrir el navegador con el driver seleccionado"""
        navigator = NavigatorDriver()
        self.error = navigator.error
        logger.info(navigator.driver.title)
        if not self.error:
            self.driver = navigator.driver
            self.driver.get("https://web.whatsapp.com")


class SendMessageWorker(QRunnable):
    def __init__(self, driver, phones, message, **kwargs):
        super(SendMessageWorker, self).__init__()
        self._phones = phones
        self._message = message
        self._driver = driver
        self.signals = WorkerSignals()
        self.kwargs = kwargs
        self.kwargs["progress_bar"] = self.signals.progress

    @Slot()
    def run(self):
        total = len(self._phones)
        for id_phone, phone in enumerate(self._phones):
            phone = FilterNumbers.checking_phone(str(phone))
            message = f"{id_phone}: {self._message}"
            self.kwargs["progress_bar"].emit(id_phone/total * 100)
            if not phone:
                continue

            logger.info(f"Phone verified: {phone}")

            self._driver.get(f"https://web.whatsapp.com/send/?phone={phone}&text&type=phone_number&app_absent=0")
            time.sleep(2.5)

            try:
                alert = self._driver.switch_to.alert
            except NoAlertPresentException:
                pass
            else:
                alert.accept()

            try:
                message_box = WebDriverWait(self._driver, 30).until(
                    EC.visibility_of_element_located((
                        By.XPATH,
                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div'
                    ))
                )

            except TimeoutException:
                pass
            else:
                logger.info(message)
                message_box.send_keys(message)
                time.sleep(0.7)
                message_box.send_keys(Keys.ENTER)
                time.sleep(1.5)
        else:
            self.signals.finished.emit()
            time.sleep(3)
            self._driver.quit()


class NavigatorDriver:
    """Clase que nos permite obtener el driver del navegador que tengamos en el sistema

    Attributes:
        __driver_options (dict): Las opciones de configuración que podemos tener en windows y linux
        __os(str): Nombre del sistema operativo
        driver(webdriver. Chrome, webdriver. ChromiumEdge): Driver que se ha seleccionado
    """
    __driver_options = {
        "Chrome": {
            "driver": "Chrome",
            "data": {
                "posix": rf'/home/{os.getlogin()}/.config/google-chrome/Default',
                "nt": rf'C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data\Default'
            },
        },
        "Edge": {
            "driver": "Edge",
            "data": {
                "posix": None,
                "nt": rf'C:\Users\{os.getlogin()}\AppData\Local\Microsoft\Edge\User Data\Default'
            }
        }
    }

    def __init__(self):
        """Inicialización de la clase y la elección del driver
        """
        self.driver = None
        self.__os = os.name
        self.error = None
        self.choose_driver()

    def __driver_chrome(self):
        """Configuraciones del webdriver de Google Chrome

        Returns:
             webdriver.Chrome(): WebDriver de Chrome
        """
        logger.info("Abriendo Chrome")
        options = webdriver.ChromeOptions()
        data = self.__driver_options["Chrome"]["data"][self.__os]
        options.add_argument(rf'user-data-dir={data}')

        driver = webdriver.Chrome(options=options)
        return driver

    def __driver_edge(self):
        """Configuraciones del webdriver del navegador de windows Edge

        Returns:
            webdriver.ChromiumEdge(): WebDriver de Edge
        """
        logger.info("Abriendo Edge")
        options = webdriver.EdgeOptions()
        data = self.__driver_options["Edge"]["data"][self.__os]
        options.add_argument(rf'user-data-dir={data}')

        driver = webdriver.ChromiumEdge(options=options)
        return driver

    def choose_driver(self):
        """Nos permite escoger el navegador que tengamos en nuestro sistema, Edge, o Chrome
        """
        try:
            driver = self.__driver_chrome()
            logger.info("Chrome iniciado con éxito")
        except Exception as e:
            logger.error(e)
            try:
                driver = self.__driver_edge()
                logger.info("Edge iniciado con éxito")
            except Exception as e:
                logger.error(e)
                self.error(f"No se ha encontrado navegador compatible: {e}")
            else:
                self.driver = driver
        else:
            self.driver = driver


if __name__ == "__main__":
    pass
