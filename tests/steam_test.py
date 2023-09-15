""""Тест перехода на страницу авторизации steam"""

from pages.battle_page import BattlePage


def test_steam(driver, request):
    """Поле ввода steam на странице?"""
    page = BattlePage(driver)
    page.go_to_site()
    social = page.steam_name()

    page.screen(request, 1)
    page.click_steam_button()
    status = page.check_steam_login_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно {social} в {driver.capabilities['browserName']} прогрузилось")
