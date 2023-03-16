import time
from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def shiny_page(self):
        self.browser.find_element(By.XPATH, "//a[@class='header-nav__link']//span[contains(text(), 'Шины')]").click()
        #time.sleep(10)

    def add_to_basket(self):
        self.browser.find_element(By.XPATH, "//button[@class='product-card__button kd-btn kd-btn--small kd-btn--flex kd-btn_primary']//span[contains(text(), '11 770')]").click()
        #time.sleep(5)
        self.browser.find_element(By.XPATH, "//a[@class='kd-btn kd-btn_primary' and contains(text(), 'Перейти в корзину')]").click()

    def checkout_page(self):
        self.browser.find_element(By.XPATH, '//input[@name="ORDER_PROP_2"]').send_keys("Anastasia")
        self.browser.find_element(By.XPATH, '//input[@name="ORDER_PROP_3"]').send_keys("Nikolaevna")
        self.browser.find_element(By.XPATH, '//input[@name="ORDER_PROP_5"]').send_keys("test12@mail.ru")
        self.browser.find_element(By.XPATH, '//input[@name="ORDER_PROP_6"]').send_keys(time.strftime("%Y%m%M%S"))
        #time.sleep(5)
        self.browser.find_element(By.XPATH, "//span[contains(text(), 'Получить код')]").click()
        #time.sleep(5)
        self.browser.find_element(By.XPATH, "//input[@name='phone_validation']").send_keys(time.strftime("%m%d"))


    def success_order(self):
        self.browser.find_element(By.XPATH, "//a[@class='kd-btn kd-tabs-shop__btn kd-btn_primary' and contains(text(), 'Выбрать магазин')]").click()
        #time.sleep(10)
        self.browser.find_element(By.XPATH, "//div[@class='checkout-popup-mobile__header-text']").click()
        self.browser.find_element(By.XPATH, "//div[@class='checkout-popup-mobile__bottom--active' and contains(text(), 'Заберу отсюда')]").click()
        #time.sleep(5)
        self.browser.find_element(By.XPATH, "//div[@class='cart-payment__title' and contains(text(), 'При получении')]").click()
        #time.sleep(10)
        self.browser.find_element(By.XPATH, "//button[@class='kd-btn_wide kd-btn kd-btn_primary']").click()
        #time.sleep(5)
        assert "Спасибо, ваш заказ принят" == self.browser.find_element(By.XPATH, "//h1").text



