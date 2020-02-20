from bizone.pattern import singleton, Facade
from bizone.app_pages.facade import Page
from bizone.app_utils.xpath import Xpath
from bizone.app_const import Const
from bizone.app_utils.tabs import Tabs
from bizone.app_utils.checks import Checks


@singleton
class App(Facade):
    """ Фасад приложения """
    const = Const
    tabs = Tabs
    check = Checks
    xpath = Xpath
    page = Page()


app = App()
