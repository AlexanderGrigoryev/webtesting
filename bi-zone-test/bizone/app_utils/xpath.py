class Xpath:
    """ общие параметризированные xpath-запросы """

    @staticmethod
    def label(contain_text):
        return '//label[contains(.,"%s")]' % contain_text

    @staticmethod
    def button(contain_text):
        return './/button[contains(.,"%s")]' % contain_text

    @staticmethod
    def link(contain_text=None):
        return './/a[contains(.,"%s")]' % contain_text if contain_text else './/a'

    @staticmethod
    def p(contain_text=None):
        return './/p[contains(.,"%s")]' % contain_text if contain_text else './/p'

    @staticmethod
    def h4(contain_text):
        return './/h4[contains(.,"%s")]' % contain_text

    @staticmethod
    def ul_following():
        return './/following-sibling::ul[1]'

    @staticmethod
    def div(contain_class, contain_text):
        return '//div[contains(@class, "%s") and contains(.,"%s")]' % (contain_class, contain_text)

    @staticmethod
    def aside():
        return './/aside'

    @staticmethod
    def header():
        return './/header'

    @staticmethod
    def section():
        return './/section'

    @staticmethod
    def footer(contain_class=None):
        return './/footer[contains(@class, "%s")]' % contain_class if contain_class else './/footer'

    @staticmethod
    def blockquote(contain_text=None):
        return './/blockquote[contains(., "%s")]' % contain_text if contain_text else './/blockquote'
