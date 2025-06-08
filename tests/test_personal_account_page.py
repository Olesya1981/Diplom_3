import pytest
from pages.personal_account_page import *
from data import *
from conftest import driver

class TestPersonalAccountPage:
    @pytest.mark.parametrize(
        'urls',
        [
            Urls.main_page_url,
            Urls.order_feed_url
        ]
    )
    @allure.title("Переход по клику на личный кабинет")
    def test_move_to_personal_account_by_click(self, driver, urls):
        driver.get(urls)
        personal_account_page = PersonalAccountPage(driver)
        text = personal_account_page.move_to_personal_account_by_click()
        assert text == 'Вход'

    @allure.title("Проверяем переход в раздел 'История заказов'")
    def test_move_to_orders_history(self, driver):
        driver.get(Urls.login_page_url)
        personal_account_page = PersonalAccountPage(driver)
        element_class = personal_account_page.move_to_orders_history()
        assert element_class == "Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"

    @allure.title("Проверяем выход из аккаунта")
    def test_logout_from_account(self, driver):
        driver.get(Urls.login_page_url)
        personal_account_page = PersonalAccountPage(driver)
        text = personal_account_page.exit_from_account()
        assert text == 'Вход'
