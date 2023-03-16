import allure

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://external.kolesa-darom.ru/"

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_site(self):
        return self.driver.get(self.url)

    # def find(self, locator: tuple, time=20):
    #     with allure.step(f"Поиск элемента, который виден: {locator}"):
    #         #self.logger.info(f"Поиск элемента: {locator}")
    #         try:
    #             return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator), message=f"Элемент не виден: {locator}")
    #         except TimeoutException:
    #             allure.attach(self.browser.get_screenshot_as_png(), name=f"TimeoutException_error.png", attachment_type=allure.attachment_type.PNG)
    #             raise AssertionError(f"Элемент не виден: {locator}")
    #         except NoSuchElementException:
    #             allure.attach(self.browser.get_screenshot_as_png(), name=f"NoSuchElementException_error.png", attachment_type=allure.attachment_type.PNG)
    #             raise AssertionError(f"Элемент не виден: {locator}")

    # def go_to_site(self):
    #     with allure.step("Открываем сайт"):
    #         #self.logger.info(f"Открываем сайт: {self.url}")
    #         self.browser.get(self.url)
    #         allure.attach(self.browser.get_screenshot_as_png(), name=f"{self.browser.current_url}.png", attachment_type=allure.attachment_type.PNG)
    #         if "https://external.kolesa-darom.ru/" in self.browser.current_url:
    #             zagolovok = "Колеса Даром» — интернет-магазин шин, дисков и автотоваров в "
    #             assert zagolovok in self.browser.title, f"Заголовок должен быть: {zagolovok}, а сейчас: {self.browser.title}"




