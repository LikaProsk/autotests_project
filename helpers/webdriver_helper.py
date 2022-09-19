from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverHelper:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def check_element_on_page(self, locator):
        try:
            WebDriverWait(self.web_driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_elements(self, locator):
        self.check_element(locator)
        return self.web_driver.find_elements(locator[0], locator[1])

    def get_element(self, locator):
        self.check_element(locator)
        return self.web_driver.find_element(locator[0], locator[1])

    def get_element_by_name(self, elements_locator, name_element):
        elements = self.get_elements(elements_locator)

        result = None
        for element in elements:
            if element.text == name_element:
                result = element

        assert result is not None, f'Не удлось найти элемент с названием {name_element}'

        return result

    def set_value_in_input(self, locator, value):
        self.check_element(locator)
        element = self.get_element(locator)
        element.clear()
        element.send_keys(value)

    def click_element_with_waiting(self, locator):
        self.check_element(locator)
        el = self.web_driver.find_element(locator[0], locator[1])
        el.click()

    def check_element(self, locator):
        check_result = self.check_element_on_page(locator)
        assert check_result, f"Элемент {locator[1]} не найден"

    def get_text_element(self, locator):
        self.check_element(locator)
        el = self.web_driver.find_element(locator[0], locator[1])
        return el.text

    def check_elements(self, locators: list):
        errors = []
        for locator in locators:
            result = self.check_element_on_page(locator)
            if not result:
                errors.append(f'Элемент c локатором {locator} не найден')

        assert not len(errors), '\n'.join(errors)
