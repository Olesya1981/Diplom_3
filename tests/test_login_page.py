from pages.login_page import LoginPage
import allure
from conftest import driver
from data import *

class TestLoginPage:
    @allure.title("Проверяем переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_switching_to_the_password_recovery_page(self, driver):
        driver.get(Urls.login_page_url)
        login_page = LoginPage(driver)
        text = login_page.switching_to_the_password_recovery_page()
        assert text == 'Восстановить'

    @allure.title("Проверяем ввод почты и клик по кнопке восстановить")
    def test_enter_email_and_click_recovery_button(self, driver):
        driver.get(Urls.login_page_url)
        login_page = LoginPage(driver)
        text = login_page.enter_email_and_click_recovery_button()
        assert text == 'Сохранить'

    @allure.title("Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_the_show_hidden_button_makes_field_active(self,driver):
        driver.get(Urls.login_page_url)
        login_page = LoginPage(driver)
        element_class = login_page.click_the_show_hidden_button_makes_field_active()
        assert element_class == password_field_active