""""Негативные тесты с неверными паролями"""

from pages.battle_page import BattlePage
import pytest


@pytest.mark.parametrize("wrong_password, description", [
    ("", "пустой пароль"),
    ("qwerty123", "неверный пароль"),
    (" qwerty123$%^&", "верный пароль с пробелом в начале"),
    ("qwerty123$%^& ", "верный пароль с пробелом в конце"),
])
def test_negative_password(driver, request, wrong_password, description):
    """Ошибка пароля отображается на странице?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.send_login("citato2380@utwoko.com")
    page.send_password(wrong_password)

    page.screen(request, 1, description)
    page.click_submit_button()
    error = page.error_password_is_here()
    assert error == "Введите пароль."

    page.screen(request, 2, description)
    print(f"\nТест с неверным паролем ({description}) в {driver.capabilities['browserName']} прошёл")
    