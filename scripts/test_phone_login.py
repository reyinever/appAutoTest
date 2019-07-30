from base.read_Data import read_data
from base.init_driver import init_driver
from pages.page_obj import Page_obj
import pytest, allure
from base.public_var import screenshot_path
import os, time


def get_test_data():
    data_list = []
    datas = read_data("phone_login.yaml").get("phone_login")
    print(datas)
    for k in datas.keys():
        data_list.append((k, datas.get(k).get('phone_no'),
                          datas.get(k).get("vervify_code"),
                          datas.get(k).get("expected")))
    return data_list


class Test_phone_login:
    def setup_class(self):
        self.driver = init_driver()
        self.page_obj = Page_obj(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @allure.step(title="点击手机号登录")
    @pytest.fixture()
    def click_login_method(self):
        self.page_obj.re_login_method_page().click_phone_login()

    @allure.step(title="输入手机号登录信息")
    @pytest.mark.usefixtures("click_login_method")
    @pytest.mark.parametrize("case_no,phone_no,vervify_code,expected", get_test_data())
    def test_input_user_info(self, case_no, phone_no, vervify_code, expected):
        self.page_obj.re_phone_login_page().input_user_info(phone_no, vervify_code)
        time.sleep(2)
        assert expected == self.page_obj.re_phone_login_page().find_search_button()
        file_path = os.path.join(screenshot_path,
                                 self.__class__.__name__ + "_%s.png" % (time.strftime("%y_%d_%d__%H_%M_%S")))
        # print("file_path:",file_path)
        self.page_obj.re_phone_login_page().screen_shot(file_path)
