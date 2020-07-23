from appium import webdriver
import time
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = { 'platformName' : 'Android',
                         'platformVersion' : '5.1.1',
                         'deviceName' : '127.0.0.1:62001',
                         'appPackage' : 'com.tal.kaoyan',
                         'appActivity' : 'com.tal.kaoyan.ui.activity.SplashActivity',
                       }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        time.sleep(5)
        self.driver.close_app()

    def before_login(self):
        time.sleep(1)
        self.driver.find_element_by_id('android:id/button2').click()
        time.sleep(1)
        l = self.driver.get_window_size()
        x1 = l['width']*0.8
        y1 = l['height']*0.5
        x2 = l['width']*0.2

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

        self.assertTrue(self.driver.find_element_by_id('com.tal.kaoyan:id/date_task_layout'))
        self.driver.find_element_by_id('com.tal.kaoyan:id/date_task_layout').click()
        info = self.driver.find_element_by_id('com.tal.kaoyan:id/date_recommend_info_title')
        self.assertIn('备考', info.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)










