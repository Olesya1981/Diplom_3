import pytest
from pages.order_feed_page import *
from data import *
from conftest import driver

class TestOrderFeedPage:

    @allure.title("Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_order_details(self, driver):
        driver.get(Urls.base_url)
        order_feed_page = OrderFeedPage(driver)
        window = order_feed_page.open_order_details()
        assert window == "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"

    @allure.title(
        "Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице 'Лента заказов'")
    def test_user_orders_from_order_history_are_displayed_on_order_feed(self, driver):
        driver.get(Urls.base_url)
        order_feed_page = OrderFeedPage(driver)
        answer = order_feed_page.user_orders_from_order_history_are_displayed_on_order_feed()
        assert answer

    @pytest.mark.parametrize('counter', [OrderFeedLocators.ALL_TIME_COUNTER, OrderFeedLocators.TODAY_COUNTER])
    @allure.title("Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.title("Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_a_new_order_increments_the_counter(self, counter, driver):
        driver.get(Urls.base_url)
        order_feed_page = OrderFeedPage(driver)
        answer = order_feed_page.a_new_order_increments_the_counter(counter)
        assert answer

    @allure.title("Проверяем, что после оформления заказа его номер появляется в разделе В работе")
    def test_after_placing_an_order_its_number_appears_in_work_section(self, driver):
        driver.get(Urls.base_url)
        order_feed_page = OrderFeedPage(driver)
        answer = order_feed_page.after_placing_an_order_its_number_appears_in_work_section()
        assert answer
