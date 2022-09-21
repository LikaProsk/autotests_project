import allure

from page_elements.search_page import SearchPage
from page_object.header import HeaderObject


class SearchPageObject(HeaderObject):

    def __init__(self, wed_driver):
        super().__init__(wed_driver)
        self.search_elements = SearchPage()

    @allure.step('Проверка результатов поиска')
    def check_search(self, search_text: str):
        products = self._get_elements(self.search_elements.PRODUCTS_NAME)
        if len(products):
            for product in products:
                product_name = product.text
                assert search_text.lower() in product_name.lower(), 'В названии товара отсутствует искомое слово,\n' \
                                                                    f'Искали по слову {search_text}\'' \
                                                                    f'Название товара: {product_name}'
        raise Exception('Не удалось найти товары')
