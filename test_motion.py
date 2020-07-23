from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

desired_caps = { 'platformName' : 'Android',
                 'platformVersion' : '5.1.1',
                 'deviceName' : '127.0.0.1:62001',
                 'appPackage' : 'com.mymoney',
                 'appActivity' : 'com.mymoney.ui.splash.SplashScreenActivity'
               }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,500)

for i in range(3):
    swipeLeft()
    sleep(1)

driver.find_element_by_id('com.mymoney:id/step_fourth_begin_ssj_btn').click()  # 开始记账

driver.find_element_by_id('com.mymoney:id/no_sms_tv').click()  # 白给也不要

driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()  # 点击更多

driver.find_element_by_xpath('//android.view.View[contains(@index,10)]').click()  # 点击密码与手势密码

driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()

sleep(2)

for i in range(2):
    TouchAction(driver).press(x=544,y=735).wait(1000)\
        .move_to(x=210,y=1053).wait(1000)\
        .move_to(x=540,y=1386).wait(1000)\
        .move_to(x=869,y=1061).wait(1000)\
        .release().perform()

driver.close_app()
















