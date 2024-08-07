import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WhatsApp:
    def __init__(self):
        self.__driver = None

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=/home/jossef/.config/google-chrome/Default')

        driver = webdriver.Chrome(options=options)
        driver.get("https://web.whatsapp.com")

        self.__driver = driver

    def send_message(self, phones, message):
        """Permite el envío de mensajes mediante whatsapp web
        Args:
            phones: Lista de números de celular
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
