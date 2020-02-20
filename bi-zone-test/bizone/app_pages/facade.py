class Page:
    """ фасад страниц, частей и элементов управления web-приложения """

    __part = None
    __control = None

    __react_page = None
    __react_alt_page = None
    __react_backbone_page = None
    __react_typescript_page = None
    __react_scala_page = None

    @property
    def part(self):
        if self.__part is None:
            from app_pages.parts.facade import Part
            self.__part = Part()
        return self.__part

    @property
    def ctrl(self):
        if self.__control is None:
            from app_pages.controls.facade import Control
            self.__control = Control()
        return self.__control

    @property
    def react_page(self):
        if self.__react_page is None:
            from app_pages.react_page import ReactPage
            self.__react_page = ReactPage
        return self.__react_page

    @property
    def react_alt_page(self):
        if self.__react_alt_page is None:
            from app_pages.react_alt_page import ReactAltPage
            self.__react_alt_page = ReactAltPage
        return self.__react_alt_page

    @property
    def react_backbone_page(self):
        if self.__react_backbone_page is None:
            from app_pages.react_backbone_page import ReactBackbonePage
            self.__react_backbone_page = ReactBackbonePage
        return self.__react_backbone_page

    @property
    def react_typescript_page(self):
        if self.__react_typescript_page is None:
            from app_pages.react_typescript_page import ReactTypescriptPage
            self.__react_typescript_page = ReactTypescriptPage
        return self.__react_typescript_page

    @property
    def react_scala_page(self):
        if self.__react_scala_page is None:
            from app_pages.react_scala_page import ReactScalaPage
            self.__react_scala_page = ReactScalaPage
        return self.__react_scala_page
