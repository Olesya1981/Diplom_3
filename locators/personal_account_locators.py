from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href ='/account']")  # Кнопка личный кабинет на главной странице
    ENTER_FORM = (By.XPATH, ".//h2[text() = 'Вход']")  # 'вход' на странице входа в аккаунт
    ORDERS_HISTORY_BUTTON =(By.XPATH, ".//a[text() = 'История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")  # кнопка "выход"
