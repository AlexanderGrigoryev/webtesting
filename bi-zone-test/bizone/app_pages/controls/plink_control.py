from webium import Find
from app_pages.controls.base_control import BaseControl
from app import app


class PLinkControl(BaseControl):
    """ <a> внутри <p> """

    __link = Find(ui_type=app.page.ctrl.link, value=app.xpath.link())

    @property
    def href(self):
        return self.__link.href

    def goto(self, label=None):
        self.__link.goto(label=label)
