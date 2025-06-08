from selenium.webdriver.common.by import By

class GeneralLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href ='/account']")  # Кнопка личный кабинет на главной странице
    #ENTER_FORM = (By.XPATH, ".//h2[text() = 'Вход']")  # 'вход' на странице входа в аккаунт
    LOGIN_EMAIL_FIELD = (By.XPATH,".//input[@class='text input__textfield text_type_main-default' and @type='text' ]")  # поле ввода email
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//input[@name = 'Пароль']")  # поле ввода пароля
    LOGIN_LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # кнопка "войти"
    ORDERS_HISTORY_BUTTON = (By.XPATH, ".//a[text() = 'История заказов']")
    #ORDER_WINDOW = (By.XPATH, ".//p[@class = class='text text_type_digits-default']")
    OVERLAYING_ELEMENT = (By.XPATH, "//*[contains(@class,  'Modal_modal__loading')]"
                                    "/following::div[@class='Modal_modal_overlay__x2ZCr']")
    OVERLAYING_ELEMENT1 = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")  # кнопка "выход"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
