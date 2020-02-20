import pytest
from selenium import webdriver
import os


@pytest.fixture(scope='module')
def drv(request):
    driver_path = os.path.join(os.getcwd(), 'driver', 'chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
