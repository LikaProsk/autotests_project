from selenium.webdriver.common.by import By


class SearchPage:

    PRODUCTS_NAME = (By.XPATH, '//div[@data-widget="searchResultsV2"]//a/span')