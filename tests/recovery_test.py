""""Тест перехода на страницу восстановления пароля"""

from pages.battle_page import BattlePage


def test_recovery(driver, request):
    """Кнопка для восстановления пароля на странице?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_recovery_button()
    page.go_to_opened_window()
    status = page.check_recovery_password_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно восстановления пароля в {driver.capabilities['browserName']} прогрузилось")
