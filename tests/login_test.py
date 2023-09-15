""""Тест входа в аккаунт"""

from pages.battle_page import BattlePage
import time


def test_login(driver, request):
    """Ник активного аккаунта в правом верхнем углу страницы?"""
    page = BattlePage(driver)
    page.go_to_site()

    page.send_login("citato2380@utwoko.com")
    page.send_password("qwerty123$%^&")

    page.screen(request, 1)
    page.click_submit_button()
    key_word = "Учетная запись Battle.net"
    
    time.sleep(10)
    assert key_word == driver.title

    page.screen(request, 2)
    print(f"\nАвторизация в {driver.capabilities['browserName']} удалась")
