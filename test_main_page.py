from main_page import MainPage

#class TestOrder: - надо ли тут класс создавать?
def test_success_order(browser):
    link = "https://external.kolesa-darom.ru/"
    page = MainPage(browser, link)
    page.open()
    page.shiny_page()
    page.add_to_basket()
    page.checkout_page()
    page.success_order()

