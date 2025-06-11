from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from data import *
import allure
from locators.general_locators import GeneralLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Поиск элемента")
    def find_element(self, locator: object) -> WebElement:
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        return self.driver.find_element(*locator)

    @allure.step("Поиск элемента")
    def find_elements(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        return self.driver.find_elements(*locator)

    @allure.step("Поиск элемента с ожиданием")
    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        return self.find_element(locator)

    @allure.step("Клик по элементу")
    def click_to_element(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        return self.find_element(locator).click()

    @allure.step("Клик по элементу с ожиданием")
    def click_to_element_with_wait(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.find_element_with_wait(locator).click()

    @allure.step("Получить текст из эелемента")
    def get_text_from_element(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        return self.find_element_with_wait(locator).text

    @allure.step("Добавить текст в элемент")
    def add_text_to_element(self, locator, text):
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        return self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получить значение 'class' элемента")
    def get_attribute_class(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        element_class = self.find_element_with_wait(locator).get_attribute('class')
        return element_class


    @allure.step("Метод перемещения элемента")
    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);
                var dropEvent = new DragEvent('drop', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        destinationNode.dispatchEvent(dropEvent);

                        var dragEndEvent = new DragEvent('dragend', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragEndEvent);
                    }
                    simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                    """
        self.driver.execute_script(script, source_element, target_element)

    @allure.step("Функция drag and drop")
    def drag_n_drop(self, element_from, element_to):
        if Constant.browser_name == 'chrome':
            action = ActionChains(self.driver)
            action.drag_and_drop(element_from, element_to).perform()
        else:
            self.drag_and_drop_element(element_from, element_to)

    @allure.step('Закрывает всплывающее окно')
    def press_esc(self):
        action = ActionChains(self.driver)
        self.wait.until(expected_conditions.invisibility_of_element_located(GeneralLocators.OVERLAYING_ELEMENT))
        action.send_keys(Keys.ESCAPE).perform()

