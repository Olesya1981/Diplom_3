from selenium.webdriver.common.by import By

class OrderFeedLocators:
    FIRST_ORDER = (By.XPATH, ".//a[@class='OrderHistory_link__1iNby']")
    MODAL_WINDOW_ORDER = (By.XPATH, ".//section[@class= 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    LAST_ORDER = (By.XPATH, ".//div[@class = 'OrderHistory_orderHistory__qy1VB']/ul/li[last()]")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text() = 'Лента Заказов']") #Лента заказов
    ALL_TIME_COUNTER = (By.XPATH, ".//div[@class = 'undefined mb-15']//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_COUNTER = (By.XPATH, ".//p[@class = 'text text_type_main-medium' and text() = 'Выполнено за сегодня:']/following::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_IN_WORK = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    ORDER_NUMBER_WINDOW = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
