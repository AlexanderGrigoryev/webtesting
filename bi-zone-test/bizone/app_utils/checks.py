import allure


class Checks:

    @staticmethod
    def page_opened(page):
        with allure.step('Проверить, что открыта страница %s' % page.url):
            assert page.drv.current_url == page.url

    @staticmethod
    def link_applied(current_url, expected_url, strict=True):
        with allure.step('Проверить, что перешли по ссылке %s' % expected_url):
            assert current_url == expected_url if strict \
                else current_url == expected_url or current_url.replace('https:', 'http:').startswith(expected_url)
