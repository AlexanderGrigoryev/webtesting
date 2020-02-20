import allure
from webium import BasePage as WBasePage, Find
from webium.base_page import is_element_present
from webium.wait import wait
from bizone.app import app


class BasePage(WBasePage):
    """ общая логика для всех страниц web-приложения """

    aside = Find(ui_type=app.page.part.aside, value=app.xpath.aside())
    todos = Find(ui_type=app.page.part.todos, value=app.xpath.section())
    info = Find(ui_type=app.page.part.info, value=app.xpath.footer(contain_class='info'))

    @property
    def drv(self):
        return self._driver

    @property
    def done(self):
        from time import sleep
        sleep(2)
        return True

    def has_element(self, element, just_in_dom=False):
        return is_element_present(self, element_name=element, just_in_dom=just_in_dom)

    def exit(self):
        with allure.step('Перейти на пустую страницу'):
            self.drv.get(app.const.blank_url)
            wait(lambda: self.drv.current_url == app.const.blank_url)

    def open(self):
        with allure.step('Открыть страницу %s' % self.url):
            super().open()
            wait(lambda: self.done)

    def screen(self, attachment_name='Скриншот', save_to_file=None):
        png = self.drv.get_screenshot_as_png()
        allure.attach(png, name=attachment_name, attachment_type=allure.attachment_type.PNG)
        if save_to_file:
            self.drv.save_screenshot(save_to_file)
        return png
