import re


class FilterNumbers:
    """Clase que contiene métodos que nos permite filtrar los números de teléfonos."""

    @staticmethod
    def checking_phone(number: str) -> (bool, str):
        """Revisa si un número de teléfono esta correcto

        Args:
            number (str): Número de teléfono

        Returns:
            bool: true, false

        """
        number = number.strip().replace(" ", "")

        regex = r"^(\+51)?9\d{8}$"
        result = re.search(regex, number)
        if result is None:
            return
        return FilterNumbers.adapt_phone(number)

    @staticmethod
    def adapt_phone(number: str) -> str:
        if number.startswith("9"):
            number = "+51" + number
        return number

    @staticmethod
    def checking_phones(numbers: list) -> list[str]:
        numbers_adap = map(FilterNumbers.checking_phone, numbers)

        return list(numbers_adap)


if __name__ == "__main__":
    numbers = ["957657540", "+51 957657540", "1235456", "957 765 789"]
    numbers = FilterNumbers.checking_phones(numbers)
    print(numbers)
