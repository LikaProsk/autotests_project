from selenium.webdriver.common.by import By


class ProductPage:
    PRODUCT_TITLE = (By.XPATH, '//div[@data-widget="webProductHeading"]//h1')
