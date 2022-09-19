import allure

from page_object.category_page import CategoryPageObject


@allure.epic('Проверка страницы категории')
class TestCategoryPage:

    @allure.title('Проверка наличия элементов блока промокода')
    def test_checking_for_block_promo_items(self, web_driver):
        category_page_object = CategoryPageObject(web_driver)
        category_page_object.check_open_category('Электроника')
