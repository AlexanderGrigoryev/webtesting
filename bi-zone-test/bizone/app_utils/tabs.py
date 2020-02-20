from webium.wait import wait


class Tabs:

    def __init__(self, driver):
        self.driver = driver

    @property
    def handles(self):
        return self.driver.window_handles

    @property
    def active_tab(self):
        return self.driver.current_window_handle

    def new(self):
        self.driver.execute_script("window.open('');")

    def show(self, tab):
        self.driver.switch_to.window(tab)
        wait(lambda: tab == self.active_tab)

    def show_first(self):
        self.show(tab=self.handles[:1][0])

    def show_last(self):
        self.show(tab=self.handles[-1:][0])

    def close(self, tab=None):
        if tab:
            self.show(tab)
        self.driver.close()

    def close_all(self, tabs=None):
        for tab in tabs if tabs else self.handles[1:]:
            self.close(tab)
