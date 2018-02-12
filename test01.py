# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-02-06 18:22
# @Author  : Jackadam
# @Email   :
# @File    : test.py
# @Software: PyCharm
# !/usr/bin/env python3.2
from selenium import webdriver
tag = 'C:\Users\jacka\AppData\Local\Google\Chrome\Application'
driver=webdriver.Chrome(executable_path=tag)
driver.get('http://www.baidu.com')