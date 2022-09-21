import allure

from page_elements.header import HeaderElements
from page_object.base_page import BasePage


class HeaderObject(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.header_elements = HeaderElements()

    @allure.step('Проверка наличия элементов меню')
    def check_menu_element(self):
        self._check_elements(self.header_elements.MENU_ELEMENTS.values())

    @allure.step('Нажатие на кнопку каталога')
    def click_catalog_button(self):
        self._click_element_with_waiting(self.header_elements.BUTTON_CATALOG)

    @allure.step('Проверка наличия элементов меню кататлога')
    def check_catalog_menu_element(self):
        self._check_elements(self.header_elements.CATALOG_MENU_ELEMENTS.values())

    @allure.step('Открытие категории {name} из каталога')
    def open_category(self, name):
        self.click_catalog_button()
        if name in self.header_elements.CATALOG_MENU_ELEMENTS:
            category_locator = self.header_elements.CATALOG_MENU_ELEMENTS.get(name)
            self._click_element_with_waiting(category_locator)
        else:
            raise Exception(f'Не удалось найти элемент с именем {name} из списка '
                            f'{self.header_elements.CATALOG_MENU_ELEMENTS}')

    @allure.step('Поиск товара')
    def search_product(self, value):
        self._set_value_in_input(self.header_elements.SEARCH_INPUT, value)
        self._click_element_with_waiting(self.header_elements.BUTTON_SEARCH)

    @allure.step('Открытие списка заказов')
    def open_orderlist(self):
        self._click_element_with_waiting(self.header_elements.BUTTON_ORDERLIST)

    @allure.step('Нажатие на кнопку premium')
    def click_premium_button(self):
        self._click_element_with_waiting(self.header_elements.MENU_ELEMENTS.get('Premium'))
