from base.base import Base
import pages


class Post_page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_post_button(self):
        self.click_element(pages.post_button)

    def click_next(self):
        self.click_element(pages.next_button)
