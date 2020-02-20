from selenium.webdriver.remote.webelement import WebElement
from webium.base_page import is_element_present


class BasePart(WebElement):
    """ общая логика для частей страниц web-приложения """

    @property
    def drv(self):
        return self.parent

    def has_element(self, element, just_in_dom=False):
        return is_element_present(self, element_name=element, just_in_dom=just_in_dom)
