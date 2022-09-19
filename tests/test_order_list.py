import allure

from page_object.header import HeaderObject
from page_object.orderlist_page import OrderListPageObject


@allure.epic('Проверка списка заказов')
class TestSearch:

    @allure.title('Проверка открытия списка заказов неавторизованным пользователем')
    def test_open_orders_with_unauthorized_user(self, web_driver):
        header = HeaderObject(web_driver)
        header.open_orderlist()
        order_list_page_object = OrderListPageObject(web_driver)
        order_list_page_object.check_unauthorized()
