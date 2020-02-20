from bizone.app_pages.base_page import BasePage
from bizone.app import app


class ReactPage(BasePage):

    def __init__(self, driver):
        super(ReactPage, self).__init__(driver=driver, url=app.const.base_url + 'examples/react/#/')
