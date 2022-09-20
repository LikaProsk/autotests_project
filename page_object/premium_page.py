import allure

from page_elements.premium_page import PremiumPage
from page_object.header import HeaderObject


class PremiumPageObject(HeaderObject):

    def __init__(self, wed_driver):
        super().__init__(wed_driver)
        self.premium_page_elements = PremiumPage()

    @allure.step('Проверка наличия элементов блока лендинга премиум')
    def check_block_premium_elements(self):
        self.helper.check_elements(self.premium_page_elements.PREMIUM_LANDING.values())

    @allure.step('Проверка текста блока лендинга премиум')
    def check_text_lending(self, list_text: list):
        text_privilege = self.helper.get_elements(self.premium_page_elements.PREMIUM_LANDING.get('text_privilege'))
        result = [text.text in list_text for text in text_privilege]
        assert all(result), 'Не все тексты соответствуют ожиднию'
