from time import sleep

import allure

from helpers.webdriver_helper import WebDriverHelper
from page_elements.header import HeaderElements


class HeaderObject:

    def __init__(self, wed_driver):
        self.web_driver = wed_driver
        self.header_elements = HeaderElements()
        self.helper = WebDriverHelper(self.web_driver)

    @allure.step('Проверка наличия элементов меню')
    def check_menu_element(self):
        self.helper.check_elements(self.header_elements.MENU_ELEMENTS.values())

    @allure.step('Нажатие на кнопку каталога')
    def click_catalog_button(self):
        self.helper.click_element_with_waiting(self.header_elements.BUTTON_CATALOG)

    @allure.step('Проверка наличия элементов меню кататлога')
    def check_catalog_menu_element(self):
        self.helper.check_elements(self.header_elements.CATALOG_MENU_ELEMENTS.values())

    @allure.step('Открытие категории {name} из каталога')
    def open_category(self, name):
        self.click_catalog_button()
        if name in self.header_elements.CATALOG_MENU_ELEMENTS:
            category_locator = self.header_elements.CATALOG_MENU_ELEMENTS.get(name)
            self.helper.click_element_with_waiting(category_locator)
        else:
            raise Exception(f'Не удалось найти элемент с именем {name} из списка '
                            f'{self.header_elements.CATALOG_MENU_ELEMENTS}')

    @allure.step('Поиск товара')
    def search_product(self, value):
        self.helper.set_value_in_input(self.header_elements.SEARCH_INPUT, value)
        self.helper.click_element_with_waiting(self.header_elements.BUTTON_SEARCH)

    @allure.step('Открытие списка заказов')
    def open_orderlist(self):
        self.helper.click_element_with_waiting(self.header_elements.BUTTON_ORDERLIST)

