from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("44444")
driver.maximize_window()
driver.implicitly_wait(2)

Account_text_frame = driver.find_element(
    'xpath',
    '//*[@id="app"]/div/div/div/form/div[1]/div/div/span/span/input'
)
Account_text_frame.send_keys(222222)
Password_text_frame = driver.find_element(
    'xpath',
    '//*[@id="app"]/div/div/div/form/div[2]/div/div/span/span/input'
)
Password_text_frame.send_keys('55555')
login_btn = driver.find_element(
    'xpath',
    '//*[@id="app"]/div/div/div/form/div[4]/div/div/span/button'
)
login_btn.click()
driver.implicitly_wait(5)

# 获取个人中心名字
Account_name = driver.find_element(
    "xpath",
    '//*[@id="app-content"]/div[1]/div[1]/div[2]/div[1]/div'
)
if Account_name.text == '否是否是否':
    print('sign up success!')
else:
    print('sign up not success!')

# 进去企业
lead_btn = driver.find_element(
    'xpath',
    '//*[@id="app-content"]/div[1]/div[2]/div[1]/div/div[2]/button[2]'
)
lead_btn.click()
driver.implicitly_wait(2)
user_name = driver.find_element(
    'xpath',
    '//*[@id="app-header"]/ul/li[12]/div/div/span'
).text
if user_name == "333":
    print("Enter enterprise success!")
else:
    print("Enter enterprise failure!")

# 进入企业查询首页,完成搜索功能
customer_seeking_menu = driver.find_element(
    'xpath',
    '//*[@id="/customer-seeking$Menu"]/li[1]/div/span'
)
customer_seeking_menu.click()
driver.implicitly_wait(5)
print(222222222222)
# 通过父级定位子级位置
customer_seeking_text_frame = driver.find_element_by_xpath(
    '//*[@class="_1mqUd"]/div/div/div/ul/li/div/span[1]/input'
)
customer_seeking_text_frame.send_keys('北京大学出版社有限公司')
customer_seeking_text_frame.btn = driver.find_element_by_xpath(
    '//*[@class="_1mqUd"]/div/div/div/ul/li/div/span[1]/span/button'
).click()
driver.implicitly_wait(3)

lead_xpath = driver.find_element(
    'xpath',
    '//*[@id="app-content"]/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/div/div/h3/a'
)
lead = lead_xpath.text
if lead == '北京大学出版社有限公司':
    print(0)
else:
    print(222)
sleep(2)

# 获取当前的窗口
now_win_handle = driver.current_window_handle

# 进入详情页
link_test = driver.find_element_by_link_text('北京大学出版社有限公司')
# 使用鼠标事件
#ActionChains(driver).double_click(link_test).perform()
ActionChains(driver).click(link_test).perform()
sleep(2)
print(driver.title)

# 获取所有窗口
all_win_handles = driver.window_handles

# 判断当前窗口
for handle in all_win_handles:
    if handle != now_win_handle:
        driver.switch_to_window(handle)
        print(driver.title)
        page_customer_title = driver.find_element(
            'xpath',
            '//*[@id="test"]/div[2]/div[1]/div[1]/div/h1'
        ).text
        if page_customer_title == '北京大学出版社有限公司':
            print('successful')
        else:
            print('ahh....')
        sleep(2)
        # 关闭当前窗口
        driver.close()

# 返回原有窗口
driver.switch_to_window(now_win_handle)
print(driver.title)
