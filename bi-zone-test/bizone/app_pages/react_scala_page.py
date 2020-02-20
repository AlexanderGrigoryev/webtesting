from bizone.app_pages.base_page import BasePage
from bizone.app import app


class ReactScalaPage(BasePage):

    def __init__(self, driver):
        super(ReactScalaPage, self).__init__(driver=driver, url=app.const.base_url + 'examples/scalajs-react/#/')
