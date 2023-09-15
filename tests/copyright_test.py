""""Тест перехода на страницу авторских прав"""

from pages.battle_page import BattlePage
import time


def test_copyright(driver, request):
    """Title соответствует странице авторских прав?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_copyright_button()
    key_word = "О Нарушении Авторского Права"

    time.sleep(5)
    page.refresh()
    assert key_word in driver.title

    page.screen(request, 2)
    print(f"\nОкно авторского права в {driver.capabilities['browserName']} прогрузилось")
    