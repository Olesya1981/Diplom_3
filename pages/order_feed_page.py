from selenium.webdriver.common.by import By
from pages.base_page import *
# from locators.general_locators import GeneralLocators
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Открытие всплывающего окна с деталями по клику на заказ")
    def open_order_details(self):
        self.user_authorization()
        self.click_to_element_with_wait(GeneralLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_to_element_with_wait(GeneralLocators.ORDERS_HISTORY_BUTTON)
        self.click_to_element_with_wait(OrderFeedLocators.FIRST_ORDER)
        return self.get_attribute_class(OrderFeedLocators.MODAL_WINDOW_ORDER)

    @allure.step("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов")
    def user_orders_from_order_history_are_displayed_on_order_feed(self):
        self.user_authorization()
        self.place_order()
        self.press_esc()
        self.click_to_element_with_wait(GeneralLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_to_element_with_wait(GeneralLocators.ORDERS_HISTORY_BUTTON)
        order_number = self.get_text_from_element(OrderFeedLocators.LAST_ORDER)[1:8]
        self.click_to_element_with_wait(OrderFeedLocators.ORDER_FEED_BUTTON)
        for i in range(1, 20):
            method, locator = OrderFeedLocators.ORDER_FEED_LIST
            locator = locator.format(i)
            text = self.get_text_from_element((method, locator))
            if text[1:8] == order_number:
                return True
        return False

    @allure.step("При создании нового заказа счётчик увеличивается")
    def a_new_order_increments_the_counter(self, counter):
        self.click_to_element(OrderFeedLocators.ORDER_FEED_BUTTON)
        orders_count1 = self.get_text_from_element(counter)
        self.user_authorization()
        self.place_order()
        self.wait.until_not(expected_conditions.text_to_be_present_in_element(
            OrderFeedLocators.ORDER_NUMBER_WINDOW, '9999'))
        self.press_esc()
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT1))
        self.click_to_element_with_wait(OrderFeedLocators.ORDER_FEED_BUTTON)
        self.wait.until_not(expected_conditions.text_to_be_present_in_element(counter, orders_count1))
        orders_count2 = self.get_text_from_element(counter)
        return int(orders_count2) > int(orders_count1)

    @allure.step("После оформления заказа его номер появляется в разделе В работе")
    def after_placing_an_order_its_number_appears_in_work_section(self):
        self.user_authorization()
        self.place_order()
        self.wait.until_not(expected_conditions.text_to_be_present_in_element(
            OrderFeedLocators.ORDER_NUMBER_WINDOW, '9999'))
        order_number = self.get_text_from_element(OrderFeedLocators.ORDER_NUMBER_WINDOW)
        self.press_esc()
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT1))
        self.click_to_element_with_wait(OrderFeedLocators.ORDER_FEED_BUTTON)
        self.wait.until(
            expected_conditions.text_to_be_present_in_element(OrderFeedLocators.ORDER_IN_WORK, order_number))
        order_in_work = self.get_text_from_element(OrderFeedLocators.ORDER_IN_WORK)
        return int(order_number) == int(order_in_work)

    @allure.step("Создание заказа")
    def place_order(self):
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        self.click_to_element(GeneralLocators.CONSTRUCTOR_BUTTON)
        element_from = self.find_element_with_wait(GeneralLocators.CRATER_BUN)
        element_to = self.find_element_with_wait(GeneralLocators.BASKET)
        self.drag_n_drop(element_from, element_to)
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        self.click_to_element_with_wait(GeneralLocators.PLACE_ORDER_BUTTON)
