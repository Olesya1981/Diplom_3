from pages.base_page import *
import allure
from locators.personal_account_locators import *


class PersonalAccountPage(BasePage):
    @allure.step(" Переход по клику на Личный кабинет")
    def move_to_personal_account_by_click(self):
        self.wait.until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON))
        self.click_to_element_with_wait(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait.until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.ENTER_FORM))
        return self.get_text_from_element(PersonalAccountLocators.ENTER_FORM)


    @allure.step("Переход в раздел 'История заказов'")
    def move_to_orders_history(self):
        self.user_authorization()
        self.click_to_element_with_wait(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_to_element_with_wait(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)
        element_class = self.get_attribute_class(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)
        return element_class

    @allure.step("Выход из аккаунта")
    def exit_from_account(self):
        self.user_authorization()
        self.click_to_element_with_wait(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_to_element_with_wait(PersonalAccountLocators.LOGOUT_BUTTON)
        return self.get_text_from_element(PersonalAccountLocators.ENTER_FORM)








