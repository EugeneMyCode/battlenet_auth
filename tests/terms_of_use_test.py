""""Тест перехода на страницу лицензионного соглашения"""

from pages.battle_page import BattlePage
import time


def test_terms_of_use(driver, request):
    """Title соответствует странице лицензионного соглашения?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_terms_of_use_button()
    key_word = "Лицензионное Соглашение"

    time.sleep(5)
    page.refresh()
    assert key_word in driver.title

    page.screen(request, 2)
    print(f"\nОкно лицензионного соглашения в {driver.capabilities['browserName']} прогрузилось")
    