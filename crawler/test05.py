# !/usr/bin/python
# -*- coding: UTF-8 -*-


import os
from selenium import webdriver
import config


'''
    Python爬虫：学习Selenium并使用Selenium模拟登录知乎
    
    存在问题，需要输入验证码，无法登陆
'''

# 知乎的用户名和密码

# ，获取浏览器的驱动，这里需要提前给firefox指定环境变量，如果没有指定则需要指定路径
driver = webdriver.Firefox(executable_path='F:\developer\python\geckodriver-v0.23.0-win64\geckodriver.exe')

# 窗口最大化
driver.maximize_window()

# 打开登录页面
driver.get("https://www.zhihu.com/signup?next=%2F")

# 切换到登录页面
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()

# 给输入框赋值
driver.find_element_by_xpath(
    '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(config.USERNAME)
driver.find_element_by_xpath(
    '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(config.PASSWORD)

# 模拟点击事件
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()

print driver.title
os.system("pause")
