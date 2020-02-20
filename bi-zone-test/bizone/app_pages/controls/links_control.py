from webium import Find, Finds
from app_pages.controls.base_control import BaseControl
from app import app


class LinksControl(BaseControl):
    """ список ссылок под заголовком """

    __ul = Find(value=app.xpath.ul_following())
    links = Finds(ui_type=app.page.ctrl.link, value=app.xpath.link(), context=__ul)
