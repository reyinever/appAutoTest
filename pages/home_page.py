from base.base import Base
import pages
import time


class Home_page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_home_button(self):
        self.click_element(pages.home_button)

    def click_like(self):
        print(self.find_element_o(pages.like_no).text)
        self.click_element(pages.like_button)
        time.sleep(2)
        print(self.find_element_o(pages.like_no).text)
        time.sleep(2)
