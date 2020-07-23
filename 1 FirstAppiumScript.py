from appium import webdriver

# app服务关键字
desired_capability = {'platformName' : 'Android', # 平台名称
                      'platformVersion' : '5.1.1', # 操作系统版本
                      'deviceName' : '127.0.0.1:62001', # 设备名称
                      'appPackage' : 'com.taobao.taobao', # app 包名
                      'appActivity' : 'com.taobao.tao.welcome.Welcome', # app activity 名称
                     }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
driver.implicitly_wait(5)
l = driver.get_window_size()
x1 = l['width']*0.5
y1 = l['height']*0.2
y2 = l['height']*0.8
driver.swipe()