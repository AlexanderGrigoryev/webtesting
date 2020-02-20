from webium import Find
from app_pages.parts.base_part import BasePart
from app import app


class AsidePart(BasePart):
    """ панель ссылок слева """

    examples = Find(ui_type=app.page.part.examples, value=app.xpath.header())
    blockquote = Find(ui_type=app.page.part.blockquote, value=app.xpath.blockquote())
    resources = Find(ui_type=app.page.ctrl.links, value=app.xpath.h4(contain_text=app.const.resources))
    community = Find(ui_type=app.page.ctrl.links, value=app.xpath.h4(contain_text=app.const.community))
    articles_title = Find(value=app.xpath.h4(contain_text=app.const.articles))
    issues = Find(ui_type=app.page.ctrl.link, value=app.xpath.link(contain_text=app.const.issues))

    @property
    def articles(self):
        if not self.has_element('articles_title'):
            return None
        return Find(ui_type=app.page.ctrl.links, value=app.xpath.h4(contain_text=app.const.articles), context=self)
