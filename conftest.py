from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver

link_EXTERNAL = "https://external.kolesa-darom.ru/"


def pytest_addoption(parser):
    parser.addoption("--link", help='Какой домен?', default=link_EXTERNAL)



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='Chrome',  # или default=None,
        help='Choose browser: Chrome, Firefox, Edge'
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',  # или default=None,
        help='Language'
    )
