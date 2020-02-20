class Control:
    """ фасад элементов управления """

    __link = None
    __links = None
    __p_link = None

    @property
    def link(self):
        if self.__link is None:
            from app_pages.controls.link_control import LinkControl
            self.__link = LinkControl
        return self.__link

    @property
    def links(self):
        if self.__links is None:
            from app_pages.controls.links_control import LinksControl
            self.__links = LinksControl
        return self.__links

    @property
    def p_link(self):
        if self.__p_link is None:
            from app_pages.controls.plink_control import PLinkControl
            self.__p_link = PLinkControl
        return self.__p_link
