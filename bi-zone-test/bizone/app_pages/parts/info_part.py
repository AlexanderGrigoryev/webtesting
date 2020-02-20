from webium import Find
from app_pages.parts.base_part import BasePart
from app import app


class InfoPart(BasePart):
    """ ссылки под списком дел """

    hint = Find(value=app.xpath.p(app.const.info_hint))
    created_by = Find(ui_type=app.page.ctrl.p_link, value=app.xpath.p(app.const.created_by))
    part_of = Find(ui_type=app.page.ctrl.p_link, value=app.xpath.p(app.const.part_of))
