""""Тест перехода на страницу регистрации"""

from pages.battle_page import BattlePage


def test_registration(driver, request):
    """Поле ввода для регистрации на странице?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_registration_button()
    status = page.check_registration_input_is_here()
    assert status == True

    page.screen(request, 2)
    print(f"\nОкно регистрации в {driver.capabilities['browserName']} прогрузилось")
