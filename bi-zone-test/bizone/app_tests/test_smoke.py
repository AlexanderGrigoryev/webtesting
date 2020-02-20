import allure
import pytest
from bizone.app import app
from bizone.app_tests.base_test import BaseTest


@allure.epic('Все тесты')
@allure.feature('Дымовое тестирование')
@pytest.mark.parametrize('page_class', [app.page.react_page,
                                        app.page.react_alt_page,
                                        app.page.react_backbone_page,
                                        app.page.react_scala_page,
                                        app.page.react_typescript_page])
class SmokeTest(BaseTest):

    @allure.story('Список дел работает')
    @allure.title('Страница открывается через адресную строку')
    def test_page_open(self, drv, page_class):
        page = page_class(drv)
        page.open()
        app.check.page_opened(page=page)

    @allure.story('Список дел работает')
    @allure.title('Ссылка на автора под списком дел работает')
    def test_info_created_by(self, drv, page_class):
        page = page_class(drv)
        page.open()
        href = page.info.created_by.href
        page.info.created_by.goto(label=app.const.created_by)
        app.check.link_applied(current_url=drv.current_url, expected_url=href, strict=False)

    @allure.story('Список дел работает')
    @allure.title('Ссылка на проект под списком дел работает')
    def test_info_part_of(self, drv, page_class):
        page = page_class(drv)
        page.open()
        href = page.info.part_of.href
        page.info.part_of.goto(label=app.const.part_of)
        app.check.link_applied(current_url=drv.current_url, expected_url=href, strict=False)

    @allure.story('Панель слева работает')
    @allure.title('Ссылки на панели работают')
    def test_aside_links(self, drv, page_class):
        page = page_class(drv)
        page.open()

        aside_links = []
        aside_links += page.aside.examples.sources
        aside_links += page.aside.examples.demos
        aside_links += [page.aside.blockquote.author]
        aside_links += page.aside.resources.links
        aside_links += page.aside.community.links
        aside_links += page.aside.articles.links if page.aside.articles else []
        aside_links += [page.aside.issues]
        tabs = app.tabs(drv)
        try:
            for link in aside_links:
                href = link.href
                link.open()
                app.check.link_applied(current_url=drv.current_url, expected_url=href, strict=False)
                tabs.show_first()
        finally:
            tabs.close_all()
