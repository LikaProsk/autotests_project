import os
import pickle

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ozon.ru", help="url сайта")
    parser.addoption("--browser", action="store", default="chrome", help="браузер для запуска")
    parser.addoption("--executor", action="store", default="selenoid")
    parser.addoption("--drivers", action="store", default="drivers", help="путь до webdriver")


@pytest.fixture()
def web_driver(request, url):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    executor = request.config.getoption("--executor")

    if executor == 'localhost' or executor == '127.0.0.1':
        if browser == "chrome":
            service = ChromiumService(executable_path=get_root_dir() + "/" + drivers + "/chromedriver")
            driver = webdriver.Chrome(service=service)
        elif browser == "firefox":
            service = FFService(executable_path=drivers + "/geckodriver")
            driver = webdriver.Firefox(service=service)
        elif browser == "opera":
            driver = webdriver.Opera(executable_path=drivers + "/operadriver")
        else:
            driver = webdriver.Safari()
    else:
        executor_url = f'http://{executor}:4444/wd/hub'
        caps = {
            'browserName': browser
        }
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.url = url

    return driver


def get_root_dir():
    return os.path.dirname(__file__)


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'web_driver' in item.fixturenames:
                    web_driver = item.funcargs['web_driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
