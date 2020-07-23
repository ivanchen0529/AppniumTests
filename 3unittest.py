from appium import webdriver
import unittest
import time
# import logging

class Login(unittest.TestCase):
    def setUp(self):
        # logging.info('======setUp======')
        desired_caps = {'platformName': 'Android',  # 平台名称
                        'platformVersion': '5.1',  # 系统版本
                        'deviceName': '127.0.0.1:62001',  # 设备名称
                        'appPackage': 'com.tal.kaoyan',  # apk的包名
                        'appActivity': 'com.tal.kaoyan.ui.activity.SplashActivity'  # activity名称
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # logging.info('======tearDown======')
        time.sleep(5)
        self.driver.close_app()

    def before_login(self):
        # logging.info('======test_login======')
        time.sleep(1)
        self.driver.find_element_by_id('android:id/button2').click()
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.9
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.1

        # 向左滑动3次
        for i in range(3):
            self.driver.swipe(x1, y1, x2, y1, 500)
            time.sleep(1)

        self.driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()

    def test_login_success(self):
        self.before_login()
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('ivancheny')
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('hnnj19961012')
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tal.kaoyan:id/view_wemedia_cacel').click()
        # 检查点/断言
        self.assertTrue(self.driver.find_element_by_id('com.tal.kaoyan:id/date_task_layout'))  # 判断"我知道了"是否出现
        self.driver.find_element_by_id('com.tal.kaoyan:id/date_task_layout').click()  # 点击我知道了
        info = self.driver.find_element_by_id('com.tal.kaoyan:id/date_recommend_info_title')
        self.assertIn('备考', info.text)
        # self.assertEqual('距离考研仅剩5个月？复习进度0咋办？试试这个150天规划吧！', info.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)