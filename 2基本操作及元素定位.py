from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

desired_caps = {'platformName': 'Android',  # 平台名称
                'platformVersion': '5.1',  # 系统版本
                'deviceName': '127.0.0.1:62001',  # 设备名称
                'appPackage': 'com.tal.kaoyan',  # apk的包名
                'appActivity': 'com.tal.kaoyan.ui.activity.SplashActivity'  # activity名称
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 强制等待
sleep(2)
# 隐式等待
driver.implicitly_wait(5)
# 显式等待
WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('android:id/button2'))

# 屏幕快照
driver.save_screenshot('image1.png')  # 与当前脚本同一路径
driver.get_screenshot_as_file('./image/image2.png')  # 在image文件夹中

# id定位
driver.find_element_by_id('android:id/button2').click()  # 点击"取消"按钮
sleep(1)

# 滑动
# swipe(start_x, start_y, end_x, end_y, duration) duration是间隔时间，单位ms
# 1.水平滑动
# 向左滑
l = driver.get_window_size()  # 获取界面尺寸
x1 = l['width']*0.8
y1 = l['height']*0.5
x2 = l['width']*0.2

for i in range(3):
    driver.swipe(x1, y1, x2, y1, 500)
    sleep(1)

# 向右滑
# l = driver.get_window_size()  # 获取界面尺寸
# x1 = l['width']*0.15
# y1 = l['height']*0.5
# x2 = l['width']*0.85
# driver.swipe(x1, y1, x2, y1, 500)

# 2.垂直滑动
# 向上滑
# l = driver.get_window_size()  # 获取界面尺寸
# x1 = l['width']*0.5
# y1 = l['height']*0.9
# y2 = l['height']*0.1
# driver.swipe(x1, y1, x1, y2, 500)

# 向下滑
# l = driver.get_window_size()  # 获取界面尺寸
# x1 = l['width']*0.5
# y1 = l['height']*0.3
# y2 = l['height']*0.7
# driver.swipe(x1, y1, x1, y2, 500)

driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()  # 点击"立即体验"按钮

# 登录
# driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('ruima2020')
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('1234ruima')
# driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
#
# driver.find_element_by_id('com.tal.kaoyan:id/view_wemedia_cacel').click()  # 关闭广告
#
# driver.find_element_by_id('com.tal.kaoyan:id/date_task_layout').click()  # 点击"我知道了"按钮

# text定位  appium1.5废弃
# driver.find_element_by_name('考研帮用户名/邮箱').send_keys('ruima2020')  # InvalidSelectorException

# class定位 有重复
# driver.find_element_by_class_name('android.widget.EditText').send_keys('ruima2020')
# driver.find_element_by_class_name('android.widget.EditText').send_keys('1234ruima')

# 层级定位
# 通过父节点的元素属性，减少子节点元素属性重复的可能性。
# driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()  # 点击"立即注册"按钮
# parent = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')  # 有id的父节点
# parent.find_element_by_class_name('android.widget.ImageView').click()  # 选中"头像"

# list定位
# 对一组属性完全相同的元素定位，可以先定位到这组元素上，再通过列表下标来定位其中的具体某个元素。
# images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')  # 定位一组图片元素
# images[2].click()  # 选中第3张图片
# driver.find_element_by_id('com.tal.kaoyan:id/save').click()  # 点击"保存"按钮

# xpath定位
# 绝对路径xpath执行效率较低，一般使用较少，通常使用xpath相对路径和属性定位。
# xpath路径表达式  / 从根节点选取  //从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
# nodename 选取此节点的所有子节点  . 选取当前节点  .. 选取当前节点的父节点  @ 选取属性
# xpath匹配符  * 匹配任何元素节点  @* 匹配任何元素节点  node()匹配任何类型的节点
# text          //*[@text='text文本属性']
# id            //*[@resource-id='id属性']
# class         //class属性 或者 //*[@class='class属性']
# content-desc  //*[@content-desc='desc文本']
# contains模糊定位      //*[contains(@text, 'text文本')]
# 定位一组元素效率突出  //*[contains(@content-desc, 'desc文本')]
# 	                   //*[contains(@resource-id, 'id属性')]
#                      //*[contains(@clsss, 'class属性')]
# driver.find_element_by_xpath("//android.widget.EditText[@text='考研帮用户名/邮箱']").send_keys('ruima2020')
# driver.find_element_by_xpath("//*[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys('1234ruima')
# driver.find_element_by_xpath("//*[contains(@text, '登录')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@text, '登录')]").click()
# driver.find_element_by_xpath("//android.widget.Button").click()

# uiautomator定位
# 通过android sdk自带的uiautomator库定位元素 这是android特有的定位方法
# resource-id定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('ivancheny')
# class定位
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().className("android.widget.EditText")').send_keys('ruima2020')
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('hnnj19961012')
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()