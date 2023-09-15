""""Тест перехода на страницу авторизации nintendo"""

from pages.battle_page import BattlePage


def test_nintendo(driver, request):
    """Поле ввода nintendo тут?"""
    page = BattlePage(driver)
    page.go_to_site()
    social = page.nintendo_name()

    page.screen(request, 1)
    page.click_nintendo_button()
    status = page.check_nintendo_login_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно {social} в {driver.capabilities['browserName']} прогрузилось")
