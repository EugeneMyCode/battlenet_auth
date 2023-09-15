""""Вебдрайвер и его настройки"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    """"Запуск драйвера для каждого теста в каждом браузере по очереди"""
    if request.param == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    if request.param == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService('geckodriver.exe'), options=options)
    yield driver
    driver.quit()
