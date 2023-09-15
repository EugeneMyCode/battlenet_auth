""""Тест перехода на страницу авторизации apple"""

from pages.battle_page import BattlePage


def test_apple(driver, request):
    """Поле ввода apple на странице?"""
    page = BattlePage(driver)
    page.go_to_site()
    social = page.apple_name()

    page.screen(request, 1)
    page.click_apple_button()
    status = page.check_apple_input_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно {social} в {driver.capabilities['browserName']} прогрузилось")
