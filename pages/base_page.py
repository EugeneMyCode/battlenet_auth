""""Базовый класс с методами для работы на страницах"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """"Модель страницы"""

    def __init__(self, driver):
        """"Инициализация вебдрайвера и часто используемых классов вебдрайвера"""
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 20)

    def find_element(self, locator):
        """"Поиск элемента по локатору"""
        return self._wait.until(EC.presence_of_element_located(locator), message='Элемент не найден')

    def go_to_site(self):
        """"Переход на сайт из класса потомка"""
        return self.driver.get(self.url)

    def go_to_opened_window(self):
        """"Переключение на второй таб браузера"""
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def screen(self, request, flag, arg=''):
        """"Создание скрина"""
        # Название состоит из названия тестовой функции + браузера + описания параметра в параметризованном тесте + порядковой цифры скрина в тесте
        if arg:
            self.driver.save_screenshot(f"screenshots/{request.node.originalname}-{self.driver.capabilities['browserName']}-{arg}-{flag}.png")
        # Название состоит из названия тестовой функции + браузера + порядковой цифры скрина в тесте
        else:
            self.driver.save_screenshot(f"screenshots/{request.node.originalname}-{self.driver.capabilities['browserName']}-{flag}.png")

    def refresh(self):
        """"Обновление страницы"""
        self.driver.refresh()
