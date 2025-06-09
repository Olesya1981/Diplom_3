from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")  # кнопка Конструктор на главной
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text() = 'Лента Заказов']") #Лента заказов
    INGREDIENT_BUTTON = (By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text() = 'Соус фирменный Space Sauce']")# Space sauce
    CLOSE_INGREDIENT_BUTTON = (By.XPATH, ".//button[@type = 'button' and @class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # кнопка, закр всплывающее окно
    ORDER_FEED_FORM = (By.XPATH, ".//h1[text() = 'Лента заказов']")
    INGREDIENT_WINDOW = (By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    CLOSED_INGREDIENT_WINDOW = (By.XPATH, ".//section[@class='Modal_modal__P3_V5']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    WAITING_WINDOW = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

#Каунтеры
    CRATER_BUN_COUNTER = (By.XPATH, ".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6c']//p[@class='counter_counter__num__3nue1']")

