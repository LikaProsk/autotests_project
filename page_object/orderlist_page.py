import allure

from page_elements.orderlist_page import OrderListPage
from page_object.header import HeaderObject


class OrderListPageObject(HeaderObject):

    def __init__(self, wed_driver):
        super().__init__(wed_driver)
        self.orderlist_elements = OrderListPage()

    @allure.step('Проверкак открытия заказов неавторизованным пользователем')
    def check_unauthorized(self):
        self.open_orderlist()
        text = self._get_text_element(self.orderlist_elements.TEXT_UNAUTHORIZED)
        assert text == 'Вы не авторизованы', 'Текущий текст не совпадает с ожидаемуму.\n' \
                                             'Ожидалось: Вы не авторизованы\n' \
                                             f'Фактический результат: {text}'
