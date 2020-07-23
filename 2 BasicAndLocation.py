from appium import webdriver

desired_capability = { 'platformName' : 'Android',
                       'platformVersion' : '5.1.1',
                       'deviceName' : '127.0.0.1:62001',
                       'appPackage' : 'com.tal.kaoyan',
                       'appActivity' : 'com.tal.kaoyan.ui.activity.SplashActivity'
                     }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
driver.implicitly_wait(5)

driver.find_element_by_id('android:id/button2').click()
driver.implicitly_wait(5)
l = driver.get_window_size()
x1 = l['width']*0.8
y1 = l['height']*0.5
x2 = l['width']*0.2

for i in range(3):
    driver.swipe(x1, y1, x2, y1, 500)

driver.implicitly_wait(5)
driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()

# driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('ivancheny')
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('hnnj19961012')
# driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
# driver.find_element_by_id('com.tal.kaoyan:id/view_wemedia_cacel').click()
# driver.find_element_by_id('com.tal.kaoyan:id/date_task_layout').click()

# text定位  appium1.5废弃
# driver.find_element_by_name('考研帮用户名/邮箱').send_keys('ruima2020')  # InvalidSelectorException
# driver.find_element_by_name('考研帮用户名/邮箱').send_keys('ivanchen')

# class定位 有重复
# driver.find_element_by_class_name('android.widget.EditText').send_keys('ivancheny')
# driver.find_element_by_class_name('android.widget.EditText').send_keys('hnnj19961012')

# driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
# 父子组合定位
# parent = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
# parent.find_element_by_class_name('android.widget.ImageView').click()

# list定位
# image = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
# image[2].click()
# driver.find_element_by_id('com.tal.kaoyan:id/save').click()

# text = driver.find_elements_by_class_name('android.widget.EditText')
# text[0].send_keys('ivancheny')
# text[1].send_keys('hnnj19961012')
# driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

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

# driver.find_element_by_xpath('//android.widget.EditText[@text="考研帮用户名/邮箱"]').send_keys('ivancheny')
# driver.find_element_by_xpath('//*[@resource-id="com.tal.kaoyan:id/login_password_edittext"]').send_keys('hnnj19961012')
# driver.find_element_by_xpath('//*[contains(@text,"登录")]').click()
# driver.find_element_by_xpath('//android.widget.Button[contains(@text,"登录")]').click()
# driver.find_element_by_xpath('//android.widget.Button').click()

# uiautomator定位
# 通过android sdk自带的uiautomator库定位元素 这是android特有的定位方法
# resource-id定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('ivan')
# class定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('ivancheny')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('hnnj19961012')
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()



















