import allure

from page_elements.category_page import CategoryPageElements
from page_object.header import HeaderObject


class CategoryPageObject(HeaderObject):

    def __init__(self, wed_driver):
        super().__init__(wed_driver)
        self.category_elements = CategoryPageElements()

    @allure.step('Проверка открытия категории')
    def check_open_category(self, name):
        self.open_category(name)
        self.check_title_category(name)

    @allure.step('Проверка заголовка категории')
    def check_title_category(self, title):
        page_title = self._get_text_element(self.category_elements.TITLE_CATEGORY)
        assert page_title == title, 'Текущий заголовок категории не совпадает с ожидаемуму.\n' \
                                    f'Ожидалось: {title}\n' \
                                    f'Фактический результат: {page_title}'
