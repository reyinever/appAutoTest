from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Base():
    def __init__(self, driver):
        self.driver = driver

    def find_element_o(self, location, timeout=8, poll=0.5):
        """
        :param location: 元组(定位方式,定位表达式) 如：(By.Id，ID属性值)
        :param timeout: 超时时间
        :param poll: 时间间隔
        :return: 定位对象
        """
        try:
            return WebDriverWait(self.driver, timeout, poll). \
                until(lambda x: x.find_element(*location))
        except Exception as e:
            print("定位元素异常：", e.args)
            raise e

    def find_elements_o(self, location, timeout=8, poll=1):
        """
        :param location: 元组(定位方式,定位表达式)
        :param timeout: 超时时间
        :param poll: 时间间隔
        :return: 定位一组对象
        """
        try:
            return WebDriverWait(self.driver, timeout, poll). \
                until(lambda x: x.find_elements(*location))
        except Exception as e:
            print("定位一组元素异常：", e)
            raise e

    def exist_element(self, location):
        """
        判断元素是否存在
        :param location_method:
        :param location_expression:
        :return:
        """
        try:
            if self.find_element_o(location):
                return True
        except Exception as e:
            print("判断元素是否存在异常：", e)
            return False

    def click_element(self, location):
        # 点击元素
        try:
            self.find_element_o(location).click()
        except Exception as e:
            print("点击元素异常：", e)
            raise e

    def input_element(self, location, content):
        # 输入内容
        try:
            element = self.find_element_o(location)
            element.clear()
            sleep(1)
            element.send_keys(content)
        except Exception as e:
            print("输入内容异常：", e)
            raise e

    def drag_element(self, location1, location2):
        try:
            e1 = self.find_element_o(location1)
            e2 = self.find_element_o(location2)
            self.driver.drag_and_drop(e1, e2)
        except Exception as e:
            print('拖拽元素异常：', e)
            raise e

    def screen_shot(self, file_path):
        self.driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    # from base.init_driver import init_driver
    from init_driver import init_driver
    import time

    driver = init_driver()
    base = Base(driver)
    # e = base.find_element_o(("id", "com.android.contacts:id/menu_add_contact"))
    # e.click()
    time.sleep(2)
    base.screen_shot("abc.png")
    time.sleep(3)
    driver.quit()
