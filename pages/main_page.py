from pages.base_page import *
from locators.general_locators import *
import allure
from locators.main_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):

    @allure.step("Переход по клику на конструктор")
    def move_to_constructor_by_click(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.get_text_from_element(MainPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step("Переход по клику на Ленту заказов")
    def move_to_order_feed_by_click(self):
        self.click_to_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)
        return self.get_text_from_element(MainPageLocators.ORDER_FEED_FORM)


    @allure.step("Открытие всплывающего окна ингредиента")
    def ingredient_window_open_by_click(self):
        self.click_to_element_with_wait(MainPageLocators.INGREDIENT_BUTTON)
        element_class = self.get_attribute_class(MainPageLocators.CLOSE_INGREDIENT_BUTTON)
        return element_class


    @allure.step("Всплывающее окно закрывается кликом по крестику")
    def ingredient_window_close_by_click(self):
        self.click_to_element_with_wait(MainPageLocators.INGREDIENT_BUTTON)
        self.click_to_element_with_wait(MainPageLocators.CLOSE_INGREDIENT_BUTTON)
        number = len(self.find_elements(MainPageLocators.CLOSED_INGREDIENT_WINDOW))
        return number


    @allure.step("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def adding_an_ingredient_to_an_order_increases_the_counter_of_this_ingredient(self):
        element_value = self.get_text_from_element(MainPageLocators.CRATER_BUN_COUNTER)
        element_from = self.find_element_with_wait(MainPageLocators.CRATER_BUN)
        element_to = self.find_element_with_wait(MainPageLocators.BASKET)
        self.drag_n_drop(element_from, element_to)
        element_value_new = self.get_text_from_element(MainPageLocators.CRATER_BUN_COUNTER)
        return element_value, element_value_new


    @allure.step("Залогиненный пользователь может оформить заказ")
    def an_authorized_user_can_place_an_order(self):
        self.user_authorization()
        self.place_order()
        self.wait.until_not(expected_conditions.text_to_be_present_in_element(
            MainPageLocators.WAITING_WINDOW, '9999'))
        text = self.get_text_from_element(MainPageLocators.WAITING_WINDOW)
        return text


    @allure.step('Закрывает всплывающее окно')
    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
