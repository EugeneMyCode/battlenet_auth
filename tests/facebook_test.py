""""Тест перехода на страницу авторизации facebook"""

from pages.battle_page import BattlePage


def test_facebook(driver, request):
    """Поле ввода facebook на странице?"""
    page = BattlePage(driver)
    page.go_to_site()
    social = page.facebook_name()

    page.screen(request, 1)
    page.click_facebook_button()
    status = page.check_facebook_input_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно {social} в {driver.capabilities['browserName']} прогрузилось")
