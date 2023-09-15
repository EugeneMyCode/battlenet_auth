""""Тест перехода на страницу параметров куков"""

from pages.battle_page import BattlePage


def test_cookie_params(driver, request):
    """Кнопка подтверждения параметров куков присутствует?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_cookie_params_button()
    status = page.check_cookie_params_button_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно параметров куков в {driver.capabilities['browserName']} прогрузилось")
    