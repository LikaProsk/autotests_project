import allure

from page_object.header import HeaderObject


@allure.epic('Проверка шапки страницы')
class TestHeader:

    @allure.title('Проверка наличия элементов меню')
    def test_checking_for_menu_items(self, web_driver):
        header = HeaderObject(web_driver)
        header.check_menu_element()

    @allure.title('Проверка наличия элементов каталога')
    def test_checking_for_catalog_items(self, web_driver):
        header = HeaderObject(web_driver)
        header.click_catalog_button()
        header.check_catalog_menu_element()
