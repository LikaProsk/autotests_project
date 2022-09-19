from selenium.webdriver.common.by import By


class HomePageElements:
    BLOCK_PROMO = {
        'Title': (By.XPATH, '//div[@data-widget="promoNavigation"]/p'),
        'Поля ввода промокода': (By.XPATH, '//div[@data-widget="promoNavigation"]//input'),
        'Отправка промокода': (By.XPATH, '//div[@data-widget="promoNavigation"]//button'),
        'Все акции и купоны': (By.LINK_TEXT, 'Все акции и купоны')
    }

    BLOCK_AUTH = {
        'Title': (By.XPATH, '//div[@data-widget="authorization"]/p[1]'),
        'Описание': (By.XPATH, '//div[@data-widget="authorization"]/p[2]'),
        'Кнопка Вход или регистрация': (By.XPATH, '//div[@data-widget="authorization"]//button'),
    }

    TITLE_CATEGORY = (By.XPATH, '//div[@data-widget="catalogResultsHeader"]/h1')

    PRODUCTS = (By.XPATH, '//div[@data-widget="skuLine"]//a//span/span')
