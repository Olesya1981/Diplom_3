import pytest
from selenium import webdriver
import data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    data.browser_name = request.param
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()
