from selenium.webdriver.remote.webelement import WebElement
from webium.base_page import is_element_present


class BaseControl(WebElement):
    """ общая логика для элементов управления web-приложения """

    @property
    def drv(self):
        return self.parent

    @property
    def text(self):
        return self.get_attribute('innerText')

    @property
    def innerHtml(self):
        return self.get_attribute('innerHtml')

    def has_element(self, element, just_in_dom=False):
        return is_element_present(self, element_name=element, just_in_dom=just_in_dom)
