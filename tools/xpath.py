# -*- coding: utf-8 -*-
# @Time    : 2017/9/20 19:36
# @Author  : Jackadam
# @Email   : 
# @File    : xpath.py
# @Software: PyCharm
# 首页相关位置：
# 请在微信中登陆位置
username = '/html/body/div/form/div/div[1]/div[2]/div[1]/div[2]/input'
password = '/html/body/div/form/div/div[1]/div[2]/div[2]/div/input'
login = '/html/body/div/form/div/div[1]/div[2]/div[3]/span'
mryt = '/html/body/div[2]/div/div[2]/div[2]/div[1]'
tklist = '/html/body/div[2]/div[2]/ul/li/a'

hqz = '/html/body/div/div[2]/div[4]'
# question = '/html/body/div/div[2]/div[4]/div'
question = '/html/body/div/div/div[1]/div[1]/div'

# 内网练习
lx = {}
lx['place']= '/html/body/div[2]/div/div[2]/div[2]/div[1]'
lx['question']=''
# 1-6 ：A-F
lx['A'] = '/html/body/div/div[3]/table/tbody/tr/td[2]/div/div/label'
lx['B'] = '/html/body/div/div[4]/table/tbody/tr/td[2]/div/div/label'
lx['C'] = '/html/body/div/div[5]/table/tbody/tr/td[2]/div/div/label'
lx['D'] = '/html/body/div/div[6]/table/tbody/tr/td[2]/div/div/label'
lx['E'] = '/html/body/div/div[7]/table/tbody/tr/td[2]/div/div/label'
lx['F'] = '/html/body/div/div[8]/table/tbody/tr/td[2]/div/div/label'
# 确认答案
lx['confirm'] = '/html/body/div/div[10]/div'
# 下一题
lx['next'] = '/html/body/div/div[11]'
# 题目数
lx['count'] ='/html/body/div/div[2]/div[2]/span'

#微信答题用
wx={}
#随机练习位置
wx['place']='/html/body/div/div[3]/div/table/tbody/tr[1]/td[2]/img'
#题目位置
wx['question']='/html/body/div/div/div[1]/div[1]/div'

# 1-6 ：A-F
wx['A'] = '/html/body/div/div/div[1]/div[1]/div/div[1]/label'
wx['B'] = '/html/body/div/div/div[1]/div[1]/div/div[2]/label'
wx['C'] = '/html/body/div/div/div[1]/div[1]/div/div[3]/label'
wx['D'] = '/html/body/div/div/div[1]/div[1]/div/div[4]/label'
wx['E'] = '/html/body/div/div/div[1]/div[1]/div/div[5]/label'
wx['F'] = '/html/body/div/div/div[1]/div[1]/div/div[6]/label'
# 确认答案
wx['confirm'] = '.btn'
# 下一题
wx['next'] = '//*[@id="hyt"]'
# 题目数
wx['count'] ='//*[@id="zpage"]'