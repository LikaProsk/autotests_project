import allure

from page_object.home_page import HomePageObject
from page_object.product_page import ProductPageObject


@allure.epic('Проверка главной страницы')
class TestHomePage:

    @allure.title('Проверка наличия элементов блока промокода')
    def test_checking_for_block_promo_items(self, web_driver):
        home_page_object = HomePageObject(web_driver)
        home_page_object.check_block_promo_elements()

    @allure.title('Проверка наличия элементов блока авторизации')
    def test_checking_for_block_auth_items(self, web_driver):
        home_page_object = HomePageObject(web_driver)
        home_page_object.check_block_auth_elements()

    @allure.title('Проверка открытия произвольного товара')
    def test_open_random_product(self, web_driver):
        home_page_object = HomePageObject(web_driver)
        product_page_object = ProductPageObject(web_driver)
        product_name = home_page_object.open_randon_product()
        product_page_object.check_product_title(product_name)
