"""
download documents
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By


class GetData:
    """
    获取数据
    """
    def __init__(self):
        self.url = 'https://wenshu.court.gov.cn/website/wenshu/181029CR4M5A62CH/index.html?#'
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging', 'enable-automation'])
        prefs = {
            'profile.default_content_settings.popups': 0,
            'download.default_directory': 'text\\',
            "profile.default_content_setting_values.automatic_downloads": 1
        }
        options.add_experimental_option('prefs', prefs)
        self.timeout = 30
        self.driver = webdriver.Chrome(
            executable_path='C:\\Users\\cosx1\\Downloads\\chromedriver.exe',
            service_log_path=os.devnull,
            options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(self.timeout)
        self.driver.get(self.url)

    def login(self):
        """
        login
        """
        self.driver.find_element_by_id('loginLi').click()
        time.sleep(7)

        # 登录
        iframe = self.driver.find_element_by_id('contentIframe')
        WebDriverWait(self.driver, self.timeout).until(
            EC.frame_to_be_available_and_switch_to_it(iframe))
        # self.driver.switch_to.frame(iframe)
        username_input = self.driver.find_element_by_name('username')
        username_input.send_keys('your_username')
        time.sleep(3)
        passwd_input = self.driver.find_element_by_name('password')
        passwd_input.send_keys('your_password')
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/form/div[3]/span').click()

    def get_data(self):
        """
        download
        """
        self.login()

        time.sleep(2)
        search_input = self.driver.find_element_by_xpath(
            '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input')
        # WebDriverWait(self.driver, self.timeout).until(
        #     EC.visibility_of_element_located(search_input))
        search_input.click()
        search_input.send_keys('TARGET_STRING')
        self.driver.find_element_by_xpath(
            '//*[@id="_view_1540966814000"]/div/div[1]/div[3]').click()

        # 每页15结果
        selector = Select(
            self.driver.find_element_by_xpath(
                '//*[@id="_view_1545184311000"]/div[8]/div/select'))
        selector.select_by_visible_text('15')

        page = 1
        while page < 4:
            time.sleep(1)
            # 全选
            self.driver.find_element_by_id('AllSelect').send_keys(Keys.SPACE)
            time.sleep(2)
            # 全部下载 按钮
            self.driver.find_element_by_xpath(
                '//*[@id="_view_1545184311000"]/div[2]/div[4]/a[3]').click()
            time.sleep(3)
            # 下一页
            # self.driver.find_element_by_xpath(
            #     '//*[@id="_view_1545184311000"]/div[8]/a[8]').click()
            self.driver.find_element_by_partial_link_text('下一页').click()
            page += 1

        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    GET_DATA = GetData()
    GET_DATA.get_data()
