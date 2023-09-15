""""Класс для работы со страницой Battlenet"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BattlePage(BasePage):
    """"Модель страницы авторизации Battlenet"""

    GOOGLE_BUTTON = (By.ID, "google")
    GOOGLE_INPUT = (By.ID, "identifierId")
    FACEBOOK_BUTTON = (By.ID, "facebook")
    FACEBOOK_INPUT = (By.ID, "email")
    APPLE_BUTTON = (By.ID, "apple")
    APPLE_INPUT = (By.ID, "account_name_text_field")
    XBOX_BUTTON = (By.ID, "live")
    XBOX_INPUT = (By.ID, "i0116")
    PS_BUTTON = (By.ID, "psn")
    PS_INPUT = (By.NAME, "email")
    NINTENDO_BUTTON = (By.ID, "nintendo")
    NINTENDO_LOGIN = (By.ID, "authorize-login-link")
    STEAM_BUTTON = (By.ID, "steam")
    STEAM_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    REGISTRATION_BUTTON = (By.ID, "signup")
    REGISTRATION_INPUT = (By.NAME, "country")
    RECOVERY_BUTTON = (By.ID, "loginSupport")
    RECOVERY_PASSWORD = (By.CSS_SELECTOR, ".fas.fa-key")
    TERMS_OF_USE = (By.CSS_SELECTOR, "div[class='mobileFooterEnabled footer-content footer-desktop grid-container'] a:nth-child(1)")
    PRIVACY = (By.XPATH, "//div[@class='footer-links nav-left']//a[@class='nav-item nav-a'][contains(text(),'Политика конфиденциальности')]")
    CONDITIONS = (By.XPATH, "//div[@class='footer-links nav-left']//a[@class='nav-item nav-a'][contains(text(),'Условия')]")
    COPYRIGHT = (By.XPATH, "//div[@class='footer-links nav-left']//a[@class='nav-item nav-a'][contains(text(),'Авторское право')]")
    COOKIE = (By.XPATH, "//div[@class='footer-links nav-left']//a[@class='nav-item nav-a'][contains(text(),'Файлы cookie')]")
    COOKIE_PARAMS = (By.XPATH, "//div[@class='footer-links nav-left']//a[@class='nav-item nav-a'][contains(text(),'Параметры cookie')]")
    COOKIE_PARAMS_BUTTON = (By.CSS_SELECTOR, ".save-preference-btn-handler.onetrust-close-btn-handler")
    LOGIN = (By.ID, "accountName")
    PASSWORD = (By.ID, "password")
    AUTH_CHECK = (By.CSS_SELECTOR, ".Navbar-label.Navbar-accountAuthenticated")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_ZERO_LOGIN = (By.CSS_SELECTOR, ".error-helper.error-helper-accountName.status-warning")
    ERROR_LOGIN = (By.CSS_SELECTOR, ".error-helper.error-helper-accountName.status-error")
    ERROR_PASSWORD = (By.CSS_SELECTOR, ".error-helper.error-helper-password.status-warning")


    url = 'https://eu.account.battle.net/login/ru/'

    def click_google_button(self):
        """"Клик по кнопке google"""
        self.find_element(self.GOOGLE_BUTTON).click()

    def google_name(self):
        """"Получение названия google из разметки"""
        return self.find_element(self.GOOGLE_BUTTON).get_attribute("title").split()[-1]

    def check_google_input_is_here(self):
        """"Проверка доступа поля для ввода логина google"""
        return self.find_element(self.GOOGLE_INPUT).is_displayed()

    def click_facebook_button(self):
        """"Клик по кнопке facebook"""
        self.find_element(self.FACEBOOK_BUTTON).click()

    def facebook_name(self):
        """"Получение названия facebook из разметки"""
        return self.find_element(self.FACEBOOK_BUTTON).get_attribute("title").split()[-1]

    def check_facebook_input_is_here(self):
        """"Проверка доступа поля для ввода логина facebook"""
        return self.find_element(self.FACEBOOK_INPUT).is_displayed()
    
    def click_apple_button(self):
        """"Клик по кнопке apple"""
        self.find_element(self.APPLE_BUTTON).click()

    def apple_name(self):
        """"Получение названия apple из разметки"""
        return self.find_element(self.APPLE_BUTTON).get_attribute("title").split()[-1]

    def check_apple_input_is_here(self):
        """"Проверка доступа поля для ввода логина apple"""
        return self.find_element(self.APPLE_INPUT).is_displayed()

    def click_xbox_button(self):
        """"Клик по кнопке xbox"""
        self.find_element(self.XBOX_BUTTON).click()

    def xbox_name(self):
        """"Получение названия xbox из разметки"""
        name = self.find_element(self.XBOX_BUTTON).get_attribute("title").split()
        return ' '.join(name[-2:])

    def check_xbox_input_is_here(self):
        """"Проверка доступа поля для ввода логина xbox"""
        return self.find_element(self.XBOX_INPUT).is_enabled()
    
    def click_ps_button(self):
        """"Клик по кнопке ps"""
        self.find_element(self.PS_BUTTON).click()

    def ps_name(self):
        """"Получение названия ps из разметки"""
        return self.find_element(self.PS_BUTTON).get_attribute("title").split()[-1]

    def check_ps_input_is_here(self):
        """"Проверка доступа поля для ввода логина ps"""
        return self.find_element(self.PS_INPUT).is_displayed()

    def click_nintendo_button(self):
        """"Клик по кнопке nintendo"""
        self.find_element(self.NINTENDO_BUTTON).click()

    def nintendo_name(self):
        """"Получение названия nintendo из разметки"""
        return self.find_element(self.NINTENDO_BUTTON).get_attribute("title").split()[-1]

    def check_nintendo_login_is_here(self):
        """"Проверка доступа поля для кнопки входа nintendo"""
        return self.find_element(self.NINTENDO_LOGIN).is_displayed()
    
    def click_steam_button(self):
        """"Клик по кнопке steam"""
        self.find_element(self.STEAM_BUTTON).click()

    def steam_name(self):
        """"Получение названия steam из разметки"""
        return self.find_element(self.STEAM_BUTTON).get_attribute("title").split()[-1]

    def check_steam_login_is_here(self):
        """"Проверка доступа поля для кнопки входа steam"""
        return self.find_element(self.STEAM_LOGIN).is_displayed()
    
    def click_registration_button(self):
        """"Клик по кнопке регистрации"""
        self.find_element(self.REGISTRATION_BUTTON).click()

    def check_registration_input_is_here(self):
        """"Проверка доступа поля для выбора страны"""
        return self.find_element(self.REGISTRATION_INPUT).is_displayed()

    def click_recovery_button(self):
        """"Клик по кнопке восстановления пароля"""
        self.find_element(self.RECOVERY_BUTTON).click()

    def check_recovery_password_is_here(self):
        """"Проверка доступа восстановления"""
        return self.find_element(self.RECOVERY_PASSWORD).is_displayed()
    
    def click_terms_of_use_button(self):
        """"Клик по пользовательскому соглашению"""
        self.find_element(self.TERMS_OF_USE).click()

    def click_privacy_button(self):
        """"Клик по политике конфиденциальности"""
        self.find_element(self.PRIVACY).click()

    def click_conditions_button(self):
        """"Клик по условиям"""
        self.find_element(self.CONDITIONS).click()

    def click_copyright_button(self):
        """"Клик по авторским правам"""
        self.find_element(self.COPYRIGHT).click()

    def click_cookie_button(self):
        """"Клик по кукам"""
        self.find_element(self.COOKIE).click()

    def click_cookie_params_button(self):
        """"Клик по параметрам куков"""
        self.find_element(self.COOKIE_PARAMS).click()

    def check_cookie_params_button_is_here(self):
        """"Проверка наличия кнопки выбора"""
        return self.find_element(self.COOKIE_PARAMS_BUTTON).is_displayed()
    
    def send_login(self, login):
        """"Ввод логина"""
        self.find_element(self.LOGIN).send_keys(login)

    def send_password(self, password):
        """"Ввод пароля"""
        self.find_element(self.PASSWORD).send_keys(password)

    def auth_is_here(self):
        """"Проверка входа в аккаунт"""
        return self.find_element(self.AUTH_CHECK).text

    def click_submit_button(self):
        """"Клик по кнопке авторизации"""
        self.find_element(self.SUBMIT_BUTTON).click()

    def error_zero_login_is_here(self):
        """"Проверка ошибки на пустой логин"""
        return self.find_element(self.ERROR_ZERO_LOGIN).text

    def error_login_is_here(self):
        """"Проверка ошибки на неверный логин"""
        return self.find_element(self.ERROR_LOGIN).text
    
    def error_password_is_here(self):
        """"Проверка ошибки на неверный пароль"""
        return self.find_element(self.ERROR_PASSWORD).text
