""""Тест перехода на страницу соглашения"""

from pages.battle_page import BattlePage


def test_conditions(driver, request):
    """Title соответствует странице соглашения?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.screen(request, 1)
    page.click_conditions_button()
    key_word = "Соглашения Blizzard Entertainment"
    assert key_word == driver.title

    page.screen(request, 2)
    print(f"\nОкно соглашения в {driver.capabilities['browserName']} прогрузилось")
