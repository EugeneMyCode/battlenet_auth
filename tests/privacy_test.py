""""Тест перехода на страницу политики конфиденциальности"""

from pages.battle_page import BattlePage
import time


def test_privacy(driver, request):
    """Title соответствует странице политики конфиденциальности?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_privacy_button()
    key_word = "Blizzard Privacy World"

    time.sleep(5)
    page.refresh()
    assert key_word == driver.title

    page.screen(request, 2)
    print(f"\nОкно политики конфиденциальности в {driver.capabilities['browserName']} прогрузилось")
    