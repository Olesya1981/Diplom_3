from pages.base_page import *
from locators.login_page_locators import *
import allure


class LoginPage(BasePage):
    @allure.step("Клик по кнопке восстановить пароль")
    def switching_to_the_password_recovery_page(self):
        self.click_to_element_with_wait(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.find_element_with_wait(LoginPageLocators.RECOVER_BUTTON)
        text = self.get_text_from_element(LoginPageLocators.RECOVER_BUTTON)
        return text

    @allure.step("Ввод почты и клик по кнопке 'Восстановить'")
    def enter_email_and_click_recovery_button(self):
        self.click_to_element_with_wait(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, email)
        self.click_to_element_with_wait(LoginPageLocators.RECOVER_BUTTON)
        text = self.get_text_from_element(LoginPageLocators.SAVE_BUTTON)
        return text

    @allure.step("Клик по кнопке показать/скрыть пароль делает поле активным")
    def click_the_show_hidden_button_makes_field_active(self):
        self.click_to_element_with_wait(LoginPageLocators.SHOW_HIDDEN_BUTTON)
        element_class =self.get_attribute_class(LoginPageLocators.PASSWORD_FIELD)
        return element_class




