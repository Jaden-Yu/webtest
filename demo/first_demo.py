from selenium import webdriver
import time

# 创建浏览器驱动
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 定位操作的元素
text_frame = driver.find_element_by_id('kw').send_keys('小米')
test_frame_btn = driver.find_element_by_id('su').click()
time.sleep(3)
test = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/span')

if test.text == '百度为您找到相关结果约80,700,000个':
    print(34567890)
else:
    print(89)
# 退出浏览器
#driver.quit()

