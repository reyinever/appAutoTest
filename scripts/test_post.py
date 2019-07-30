from base.init_driver import init_driver
from pages.page_obj import Page_obj
import os, time
from base.public_var import screenshot_path
import pytest, allure


class Test_post():
    def setup_class(self):
        self.driver = init_driver()
        self.page_obj = Page_obj(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @allure.step(title="登录")
    @pytest.fixture()
    def phone_login(self):
        print("login")
        try:
            login_method_page = self.page_obj.re_login_method_page()
            login_method_page.click_phone_login()
            login_page = self.page_obj.re_phone_login_page()
            login_page.input_user_info("xxxx", "xxx")
            time.sleep(2)
            file_path = os.path.join(screenshot_path,
                                     self.__class__.__name__ + "_%s.png" % (time.strftime("%y_%d_%d__%H_%M_%S")))
            login_page.screen_shot(file_path)
        except Exception as e:
            print("登录异常:", e)

    @allure.step(title="测试发贴")
    @pytest.mark.usefixtures("phone_login")
    def test_send_post(self):
        post_page = self.page_obj.re_post_page()
        post_page.click_post_button()
        post_page.click_next()
        time.sleep(2)
        file_path = os.path.join(screenshot_path,
                                 self.__class__.__name__ + "_%s.png" % (time.strftime("%y_%d_%d__%H_%M_%S")))
        print(file_path)
        post_page.screen_shot(file_path)
        assert True
