from webium import Find
from app_pages.parts.base_part import BasePart
from app import app


class BlockquotePart(BasePart):
    """ цитата """

    quote = Find(value=app.xpath.p())
    author = Find(ui_type=app.page.ctrl.link, value=app.xpath.link())

    @property
    def text(self):
        return self.quote.text
