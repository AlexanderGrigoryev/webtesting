from bizone.app_pages.base_page import BasePage
from bizone.app import app


class ReactTypescriptPage(BasePage):

    def __init__(self, driver):
        super(ReactTypescriptPage, self).__init__(driver=driver, url=app.const.base_url + 'examples/typescript-react/#/')
