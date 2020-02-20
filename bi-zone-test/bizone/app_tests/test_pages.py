import allure
import pytest
from bizone.app import app
from bizone.app_tests.base_test import BaseTest


@allure.epic('Все тесты')
@allure.feature('Тестирование списка дел')
@allure.story('Список дел работатет')
@pytest.mark.parametrize('page_class', [app.page.react_page,
                                        app.page.react_alt_page,
                                        app.page.react_backbone_page,
                                        app.page.react_scala_page,
                                        app.page.react_typescript_page])
class PagesTest(BaseTest):

    @allure.title('Добавление элемента')
    def test_add_item(self, drv, page_class):
        pass

    @allure.title('Редактирование элемента')
    def test_edit_item(self, drv, page_class):
        pass

    @allure.title('Удаление элемента')
    def test_delete_item(self, drv, page_class):
        pass

    @allure.title('Перевод элемента в статус завершенных')
    def test_complete_item(self, drv, page_class):
        pass

    @allure.title('Перевод всех элементов в статус завершенных')
    def test_complete_all(self, drv, page_class):
        pass

    @allure.title('Возврат элемента в статус не завершенных')
    def test_activate_item(self, drv, page_class):
        pass

    @allure.title('Возврат всех элементов в статус не завершенных')
    def test_activate_all(self, drv, page_class):
        pass

    @allure.title('Удаление завершенных элементов')
    def test_clear_completed(self, drv, page_class):
        pass

    @allure.title('Фильтрация элементов')
    def test_filter_items(self, drv, page_class):
        pass
