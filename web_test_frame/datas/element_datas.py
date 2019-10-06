'''
    Instrutions:
        1. 设置元素定位配置参数
'''
elem_login_page = {
    'account_input':['xpath','//*[@id="app"]/div/div/div/form/div[1]/div/div/span/span/input'],
    'password_input':['xpath','//*[@id="app"]/div/div/div/form/div[2]/div/div/span/span/input'],
    'login_btn':['xpath','//*[@id="app"]/div/div/div/form/div[4]/div/div/span/button']
}

elem_private_center_page = {
    'account_name':[ "xpath",'//*[@id="app-content"]/div[1]/div[1]/div[2]/div[1]/div']
}