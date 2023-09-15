""""Негативные тесты с неверными логинами"""

from pages.battle_page import BattlePage
import pytest


@pytest.mark.parametrize("wrong_login, description", [
    ("citato2380@utwokocom", "mail без точки"),
    ("citato2380utwoko.com", "mail без @"),
    ("+7923301189", "не хватает цифры в номере"),
    ("+792330122333", "на одну цифру больше в номере"),
    ("+79233012233p", "буква затесалась в номер"),
])
def test_negative_login(driver, request, wrong_login, description):
    """Ошибка логина отображается на странице?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.send_login(wrong_login)
    page.send_password("qwerty123$%^&")

    page.screen(request, 1, description)
    page.click_submit_button()
    error = page.error_login_is_here()
    assert error == "Необходимо указать корректное имя пользователя."

    page.screen(request, 2, description)
    print(f"\nТест с неверным логином ({description}) в {driver.capabilities['browserName']} прошёл")
    