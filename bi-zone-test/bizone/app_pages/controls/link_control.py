import allure
from selenium.webdriver.common.keys import Keys
from webium.wait import wait
from app_pages.controls.base_control import BaseControl
from app import app


class LinkControl(BaseControl):
    """ ссылка <a> """

    @property
    def href(self):
        return self.get_attribute('href')

    def __goto(self, label, ctrl):
        from_url = self.drv.current_url
        label_text = '"%s"' % label if label else self.text if self.text else ''
        with allure.step('Перейти по ссылке %s [%s]' % (label_text, self.href)):
            self.send_keys(Keys.CONTROL, Keys.ENTER) if ctrl else self.click()
            app.tabs(self.drv).show_last() if ctrl else None
            wait(lambda: self.drv.current_url != from_url)

    def goto(self, label=None):
        self.__goto(label=label, ctrl=False)

    def open(self, label=None):
        self.__goto(label=label, ctrl=True)
