import allure

from page_object.header import HeaderObject
from page_object.premium_page import PremiumPageObject


@allure.epic('Проверка страници premium')
class TestPremiumPage:

    @allure.title('Проверка наличия элементов блока лендинга премиум')
    def test_checking_for_block_premium(self, web_driver):
        header = HeaderObject(web_driver)
        header.click_premium_button()
        premium_page_object = PremiumPageObject(web_driver)
        premium_page_object.check_block_premium_elements()

    @allure.title('Проверка корректности текста лендинга премиум')
    def test_check_text_lending(self, web_driver):
        header = HeaderObject(web_driver)
        header.click_premium_button()
        premium_page_object = PremiumPageObject(web_driver)
        text = [
            'бесплатная курьерская\nдоставка',
            'кино, сериалы и ТВ',
            'ранний доступ\nк распродажам',
            'экономия от подписки\nв среднем 498 ₽ в месяц']
        premium_page_object.check_text_lending(text)
