from base.base import Base
import pages
from time import sleep


class Phone_login_page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def input_user_info(self, phone_no, vervify_code):
        self.input_element(pages.phone_input, phone_no)
        sleep(1)
        self.input_element(pages.vervify_code, vervify_code)
        sleep(1)
        self.click_element(pages.login_button)
        sleep(2)

    def find_search_button(self):
        return self.exist_element(pages.search_button)
