from base.base import Base
import pages


class Login_method_page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_phone_login(self):
        # 点击手机登录
        # print("phone_login",pages.phone_login)
        self.click_element(pages.phone_login)

    def click_weixin_login(self):
        # 点击微信登录
        # print("weixin_login", pages.weixin_login)
        self.click_element(pages.weixin_login)

    def click_qq_login(self):
        # 点击qq登录
        # print("qq_login", pages.qq_login)
        self.click_element(pages.qq_login)

    def click_weibo_login(self):
        # 点击微博登录
        # print("weibo_login", pages.weibo_login)
        self.click_element(pages.weibo_login)
