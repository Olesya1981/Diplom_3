from pages.main_page import MainPage
from conftest import driver
import allure
from data import *


class TestMainPage:

    @allure.title("Проверяем переход на конструктор по клику")
    def test_move_to_constructor_by_click(self, driver):
        driver.get(Urls.base_url + Urls.login_endpoint)
        main_page = MainPage(driver)
        text = main_page.move_to_constructor_by_click()
        assert text == 'Конструктор'

    @allure.title("Проверяем переход на ленту заказов по клику")
    def test_move_to_order_feed_by_click(self, driver):
        driver.get(Urls.base_url)
        main_page = MainPage(driver)
        text = main_page.move_to_order_feed_by_click()
        assert text == 'Лента заказов'

    @allure.title("Проверяем открытие всплывающего окна по клику на ингредиент")
    def test_ingredient_windows_open_by_click(self, driver):
        driver.get(Urls.base_url)
        main_page = MainPage(driver)
        element = main_page.ingredient_window_open_by_click()
        assert element == Constant.ingredient_window_class

    @allure.title("Проверяем закрытие окна ингредиента по клику на крестик")
    def test_ingredient_window_close_by_click(self, driver):
        driver.get(Urls.base_url)
        main_page = MainPage(driver)
        number = main_page.ingredient_window_close_by_click()
        assert number == 2

    @allure.title("Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_adding_an_ingredient_to_an_order_increases_the_counter_of_this_ingredient(self, driver):
        driver.get(Urls.base_url)
        main_page = MainPage(driver)
        element_value, element_value_new = main_page.adding_an_ingredient_to_an_order_increases_the_counter_of_this_ingredient()
        assert int(element_value_new) - int(element_value) == 2

    @allure.title("Проверяем, что залогиненный пользователь может оформить заказ")
    def test_an_authorized_user_can_place_an_order(self, driver):
        driver.get(Urls.base_url)
        main_page = MainPage(driver)
        order_number = main_page.an_authorized_user_can_place_an_order()
        assert int(order_number) > 230000
