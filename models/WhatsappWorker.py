import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.logging_config import logger


class WhatsappWorker:
    """Clase que tiene los métodos para poder trabajar con WhatsappWeb"""

    def __init__(self):
        self.__driver = None
        self.error = None

    def open_whatsapp(self):
        """Nos permite abrir el navegador con el driver seleccionado"""
        navigator = NavigatorDriver()
        self.error = navigator.error
        if not self.error:
            self.__driver = navigator.driver
            self.__driver.get("https://web.whatsapp.com")

    def send_message(self, phones, message):
        """Permite el envío de mensajes mediante whatsapp web
        Args:
            phones(list): Lista de números de celular
            message(str): Mensaje que se enviara

        Returns:
            None
        """
        for phone in phones:
            self.__driver.get(f"https://web.whatsapp.com/send/?phone=+51{phone}&text&type=phone_number&app_absent=0")
            time.sleep(2)

            try:
                alert = self.__driver.switch_to.alert
            except NoAlertPresentException:
                pass
            else:
                alert.accept()

            try:
                message_box = WebDriverWait(self.__driver, 30).until(
                    EC.visibility_of_element_located((
                        By.XPATH,
                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div'
                    ))
                )

            except TimeoutException:
                pass
            else:
                message_box.send_keys(message)
                time.sleep(0.5)
                message_box.send_keys(Keys.ENTER)
                time.sleep(0.5)


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
