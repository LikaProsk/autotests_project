import allure

from page_elements.product_page import ProductPage
from page_object.header import HeaderObject


class ProductPageObject(HeaderObject):

    def __init__(self, wed_driver):
        super().__init__(wed_driver)
        self.product_elements = ProductPage()

    @allure.step('Проверка заголовка товара')
    def check_product_title(self, title):
        product_title = self._get_text_element(self.product_elements.PRODUCT_TITLE)
        assert product_title == title, 'Текущий заголовок страницы товара не совпадает с ожидаемуму.\n' \
                                       f'Ожидалось: {title}\n' \
                                       f'Фактический результат: {product_title}'
