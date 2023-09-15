""""Тест перехода на страницу авторизации xbox"""

from pages.battle_page import BattlePage


def test_xbox(driver, request):
    """Поле ввода xbox на странице?"""
    page = BattlePage(driver)
    page.go_to_site()
    social = page.xbox_name()

    page.screen(request, 1)
    page.click_xbox_button()
    status = page.check_xbox_input_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно {social} в {driver.capabilities['browserName']} прогрузилось")
