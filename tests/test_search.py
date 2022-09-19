from time import sleep

import allure

from page_object.header import HeaderObject
from page_object.search_page import SearchPageObject


@allure.epic('Проверка поиска товара')
class TestSearch:

    @allure.title('Проверка поиска товара')
    def test_check_search(self, web_driver):
        header = HeaderObject(web_driver)
        search_text = 'диск'
        header.search_product(search_text)
        search = SearchPageObject(web_driver)
        search.check_search(search_text)
