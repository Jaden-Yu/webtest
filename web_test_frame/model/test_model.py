'''
    Instrutions:
        1. 编写测试用例，使用函数封装一个完整测试步骤；
        2. 引用user_config 文件中的账号；
        3. 引用element_datas 文件中的元素；
        4. 在test_cases 文件中进行引用本文件，并进行断言
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from datas.element_datas import *
from config import user_config


def win_browser(url):
    '''
    :设置浏览器驱动
    :param url: 测试网站的url
    :return: browser
    '''
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    return browser

def browser_quit(browser):
    print('Test End')
    browser.quit()


def login(browser):
    '''登录流程'''
    Account_text_frame = browser.find_element(
        elem_login_page['account_input'][0],
        elem_login_page['account_input'][1]
    )
    Account_text_frame.send_keys(user_config.User_Account['phone'])

    Password_text_frame = browser.find_element(
        elem_login_page['password_input'][0],
        elem_login_page['password_input'][1]
    )
    Password_text_frame.send_keys(user_config.User_Account['password'])

    login_btn = browser.find_element(
        elem_login_page['login_btn'][0],
        elem_login_page['login_btn'][1]
    )
    login_btn.click()
    browser.implicitly_wait(5)
    # 获取个人中心名字
    Account_name = browser.find_element(
        elem_private_center_page['account_name'][0],
        elem_private_center_page['account_name'][1],
    ).text
    return Account_name

