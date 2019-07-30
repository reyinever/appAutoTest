from pages.login_method_page import Login_method_page
from pages.phone_login_page import Phone_login_page
from pages.home_page import Home_page
from pages.post_page import Post_page


class Page_obj():
    def __init__(self, driver):
        self.driver = driver

    def re_login_method_page(self):
        return Login_method_page(self.driver)

    def re_phone_login_page(self):
        return Phone_login_page(self.driver)

    def re_home_page(self):
        return Home_page(self.driver)

    def re_post_page(self):
        return Post_page(self.driver)
