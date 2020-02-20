class Part:
    """ фасад частей страниц web-приложения """

    __aside = None
    __todos = None
    __info = None
    __blockquote = None
    __examples = None

    @property
    def aside(self):
        if self.__aside is None:
            from app_pages.parts.aside_part import AsidePart
            self.__aside = AsidePart
        return self.__aside

    @property
    def todos(self):
        if self.__todos is None:
            from app_pages.parts.todos_part import TodosPart
            self.__todos = TodosPart
        return self.__todos

    @property
    def info(self):
        if self.__info is None:
            from app_pages.parts.info_part import InfoPart
            self.__info = InfoPart
        return self.__info

    @property
    def blockquote(self):
        if self.__blockquote is None:
            from app_pages.parts.blockquote_part import BlockquotePart
            self.__blockquote = BlockquotePart
        return self.__blockquote

    @property
    def examples(self):
        if self.__examples is None:
            from app_pages.parts.examples_part import ExamplesPart
            self.__examples = ExamplesPart
        return self.__examples
