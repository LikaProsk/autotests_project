from selenium.webdriver.common.by import By


class HeaderElements:
    MENU_ELEMENTS = {
        'Premium': (By.LINK_TEXT, 'Premium'),
        'Билеты и Отели': (By.LINK_TEXT, 'Билеты и Отели'),
        'Ozon fresh': (By.LINK_TEXT, 'Ozon fresh'),
        'Ozon Карта': (By.LINK_TEXT, 'Ozon Карта'),
        'Рассрочка': (By.LINK_TEXT, 'Рассрочка'),
        'Акции': (By.LINK_TEXT, 'Акции'),
        'Бренды': (By.LINK_TEXT, 'Бренды'),
        'Express': (By.LINK_TEXT, 'Express'),
        'Сертификаты': (By.LINK_TEXT, 'Сертификаты'),
        'Электроника': (By.LINK_TEXT, 'Электроника'),
        'Одежда и обувь': (By.LINK_TEXT, 'Одежда и обувь'),
        'Дом и сад': (By.LINK_TEXT, 'Дом и сад'),
        'Детские товары': (By.LINK_TEXT, 'Детские товары'),
        'Реферальная программа': (By.LINK_TEXT, 'Реферальная программа'),
    }

    BUTTON_CATALOG = (By.XPATH, '//div[@data-widget="catalogMenu"]//button')

    CATALOG_MENU_ELEMENTS = {
        'Электроника': (By.LINK_TEXT, 'Электроника'),
        'Одежда и обувь': (By.LINK_TEXT, 'Одежда и обувь'),
        'Дом и сад': (By.LINK_TEXT, 'Дом и сад'),
        'Детские товары': (By.LINK_TEXT, 'Детские товары'),
        'Реферальная программа': (By.LINK_TEXT, 'Реферальная программа'),
    }

    SEARCH_INPUT = (By.XPATH, '//div[@data-widget="searchBarDesktop"]//input')
    BUTTON_SEARCH = (By.XPATH, '//button[@aria-label="Поиск"]')

    BUTTON_ORDERLIST = (By.XPATH, '//div[@data-widget="orderInfo"]//span[contains(text(), "Заказы")]')
