""""Негативный тест с пустыми полями логина и пароя"""

from pages.battle_page import BattlePage


def test_login(driver, request):
    """Ошибка отображается на странице?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.send_login("")
    page.send_password("")

    page.screen(request, 1)
    page.click_submit_button()
    error = page.error_zero_login_is_here()
    assert error == "Введите имя учетной записи."

    page.screen(request, 2)
    print(f"\nТест с пустыми полями в {driver.capabilities['browserName']} прошёл")
    