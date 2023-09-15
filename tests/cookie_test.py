""""Тест перехода на страницу файлы cookie"""

from pages.battle_page import BattlePage


def test_cookie(driver, request):
    """Title соответствует странице файлов куков?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_cookie_button()
    key_word = "Файлы cookie"
    assert key_word == driver.title

    page.screen(request, 2)
    print(f"\nОкно cookie в {driver.capabilities['browserName']} прогрузилось")
    