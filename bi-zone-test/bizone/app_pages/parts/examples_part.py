from webium import Finds
from app_pages.parts.base_part import BasePart
from app import app


class ExamplesPart(BasePart):
    """ ссылки на примеры использования (заголовок в панели слева) """

    demos = Finds(ui_type=app.page.ctrl.link, value=app.xpath.link(contain_text=app.const.demo))
    sources = Finds(ui_type=app.page.ctrl.link, value=app.xpath.link(contain_text=app.const.source))
