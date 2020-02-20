from bizone.app_pages.base_page import BasePage
from bizone.app import app


class ReactAltPage(BasePage):

    def __init__(self, driver):
        super(ReactAltPage, self).__init__(driver=driver, url=app.const.base_url + 'examples/react-alt/#/')
