from selenium.webdriver.common.by import By

class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль"
    EMAIL_FIELD = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name= 'name']")
    RECOVER_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    SHOW_HIDDEN_BUTTON = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
    PASSWORD_FIELD = (By.XPATH, "//label[text()= 'Пароль'] ")

