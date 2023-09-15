""""Тест перехода на страницу авторизации ps"""

from pages.battle_page import BattlePage


def test_ps(driver, request):
    """Поле ввода ps на странице?"""
    page = BattlePage(driver)
    page.go_to_site()
    social = page.ps_name()

    page.screen(request, 1)
    page.click_ps_button()
    status = page.check_ps_input_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно {social} в {driver.capabilities['browserName']} прогрузилось")
