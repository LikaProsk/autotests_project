import random

import allure

from page_elements.home_page import HomePageElements
from page_object.header import HeaderObject


class HomePageObject(HeaderObject):

    def __init__(self, wed_driver):
        super().__init__(wed_driver)
        self.home_elements = HomePageElements()

    @allure.step('Проверка наличия элементов блока промокод')
    def check_block_promo_elements(self):
        self._check_elements(self.home_elements.BLOCK_PROMO.values())

    @allure.step('Проверка наличия элементов блока авторизации')
    def check_block_auth_elements(self):
        self._check_elements(self.home_elements.BLOCK_PROMO.values())

    @allure.step('Проверка наличия товаров')
    def check_product_elements(self):
        self._check_elements([self.home_elements.PRODUCTS])

    @allure.step('Открыть произвольный товар')
    def open_randon_product(self):
        self.check_product_elements()

        products = self._get_elements(self.home_elements.PRODUCTS)
        if len(products):
            product = products[random.randint(0, len(products))]
            name = product.text
            product.click()
            return name

        raise Exception('Не удалось найти товары')
