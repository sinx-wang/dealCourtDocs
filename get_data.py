import os
from selenium import webdriver
import time


class GetData:
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
        self.driver = webdriver.Chrome(
            executable_path='C:\\Users\\cosx1\\Downloads\\chromedriver.exe',
            service_log_path=os.devnull,
            options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element_by_id('loginLi').click()
        time.sleep(7)

        # 登录
        iframe = self.driver.find_element_by_id('contentIframe')
        self.driver.switch_to.frame(iframe)
        username_input = self.driver.find_element_by_name('username')
        username_input.send_keys('18851821816')
        time.sleep(3)
        passwd_input = self.driver.find_element_by_name('password')
        passwd_input.send_keys('DevOpswny_1')
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/form/div[3]/span').click()

    def get_data(self):
        self.login()

        search_input = self.driver.find_element_by_xpath(
            '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input')
        search_input.click()
        search_input.send_keys('贵阳银行')
        self.driver.find_element_by_xpath(
            '//*[@id="_view_1540966814000"]/div/div[1]/div[3]').click()


if __name__ == '__main__':
    GET_DATA = GetData()
    GET_DATA.login()