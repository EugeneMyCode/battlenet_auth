""""Тест перехода на страницу авторизации google"""

from pages.battle_page import BattlePage


def test_google(driver, request):
    """Поле ввода google на странице?"""
    page = BattlePage(driver)
    page.go_to_site()
    social = page.google_name()

    page.screen(request, 1)
    page.click_google_button()
    status = page.check_google_input_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно {social} в {driver.capabilities['browserName']} прогрузилось")
