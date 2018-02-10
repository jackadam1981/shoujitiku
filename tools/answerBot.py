# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-01-19 18:22
# @Author  : Jackadam
# @Email   :
# @File    : scarp.py
# @Software: PyCharm
import time, random, sys
import selenium
import tools
from selenium import webdriver
import tools.value as value
import tools.xpath as xpath
from configparser import ConfigParser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

fp_dir = os.getcwd()
fp = fp_dir + '\conf.ini'  # 定义配置文件名
conf = ConfigParser()  # 实例化
conf.read(fp)  # 打开conf


class answerBot(object):
    def __init__(self, *args, **kwargs):
        print(kwargs)


        #firefox
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", kwargs.get('user-agent'))
        self.driver = webdriver.Firefox(
            firefox_binary=kwargs.get('firefox_dir'),
            executable_path=kwargs.get('geckodriver_dir'),
            firefox_profile=profile,
        )
        #chrome
        # options = webdriver.ChromeOptions()
        # options.add_argument('user-agent=' + kwargs.get('user-agent'))
        # self.driver = webdriver.Chrome(options=options)

        # print(len(kwargs.get('cookie')))
        self.driver.get('http://' + kwargs.get('host'))
        self.driver.set_window_size('640', '960')
        c1 = kwargs.get('cookie').split(';')
        for i in c1:
            i = i.split('=')
            self.driver.add_cookie({
                'name': i[0].replace(' ', ''),
                'value': i[1],
            })
        self.driver.get('http://' + kwargs.get('host') + kwargs.get('uri'))

    # def __del__(self):
    # self.driver.quit()

    def WaitClickXPATH(self, str):
        # print('click', str)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, str))).click()

    def WaitClickCSS(self, str):
        # print('click', str)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, str))).click()

    def CheckTxt(self, str1, str2, time=60, TF=True):
        if TF == True:

            WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element((By.XPATH, str1), str2))
        else:

            WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element((By.XPATH, str1), str2))

    # 获取文字,因为排行榜会有空排名，所以try一下，
    def GetTxt(self, str):
        try:
            time.sleep(2)
            text = WebDriverWait(self.driver, 60).until(EC.visibility_of(self.driver.find_element_by_xpath(str))).text
            return text
        except:
            print('no question')
            return 0
            # 获取文字,因为排行榜会有空排名，所以try一下，

    def GetList(self, str):
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of(self.driver.find_element_by_xpath(str)))
            list = self.driver.find_elements_by_xpath(str)
            print(list)
            # list = self.driver.find_elements_by_xpath(str).text
            # print(list)

            return list
        except:
            return 0

    def GetAnswer(self):
        while True:
            time.sleep(2)
            r = self.driver.find_element_by_id('stdaan')
            text = r.get_attribute('innerHTML')
            if '答案' in text:
                answer = text[6:]
                break
            time.sleep(0.5)
        return answer

    def HX_answer(txt, type):
        gailv = random.randint(1, 100)
        if gailv < 95:
            # print('不混淆')
            return txt
        else:
            # print('混淆')
            if type == '判断题':
                #设定答案是AB，选另一个答案
                ans = 'AB'
                txt = ans.index(txt)
                if txt == 0:
                    daan = ans[1]
                else:
                    daan = ans[0]
            elif type == '单选题':
                ans = 'ABCD'
                ans = ans.replace(txt, '')
                daan = random.choice(ans)
            elif type == '多选题':
                num = random.randint(2, 4)
                ans = random.sample('ABCD', num)
                ans = str(ans).replace("'", '').replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
                daan = "".join((lambda x: (x.sort(), x)[1])(list(ans)))
            else:
                print('题目类型错误？')
                daan = txt
            return daan

    # 根据答案回答问题
    def Reply(self, dict=xpath.lx):
        print('Reply')
        question = self.GetTxt(dict['question'])
        print(question)
        if question!=0:
            print('题目长度%i,等待%i' % (len(question), 0.06 * len(question)))
            answer_type = question[1:4]
            print(answer_type)
            time.sleep(0.06 * len(question))
        else:
            time.sleep(random.randint(3,6))
        answertext = (self.GetAnswer())
        # # js = 'document.getElementById("stdaan").style.display = "block"'
        # # #js = ' $("#stdaan").show();'
        # # driver.execute_script(js)
        print('正确答案： %s      ' % answertext, end='')
        sys.stdout.flush()
        #

        # print(type(dict['A']))
        # WaitClickXPATH(dict['A'])
        if answertext == 'A':
            self.WaitClickXPATH(dict['A'])
        elif answertext == 'B':
            self.WaitClickXPATH(dict['B'])
        elif answertext == 'C':
            self.WaitClickXPATH(dict['C'])
        elif answertext == 'D':
            self.WaitClickXPATH(dict['D'])
        elif answertext == 'E':
            self.WaitClickXPATH(dict['D'])
        elif answertext == 'F':
            self.WaitClickXPATH(dict['F'])
        elif answertext == '正确':
            self.WaitClickXPATH(dict['A'])
        elif answertext == '错误':
            self.WaitClickXPATH(dict['B'])
        else:
            # 多选的题目，遍历答案，逐个点选
            for i2 in answertext:
                if i2 == 'A':
                    self.WaitClickXPATH(dict['A'])
                elif i2 == 'B':
                    self.WaitClickXPATH(dict['B'])
                elif i2 == 'C':
                    self.WaitClickXPATH(dict['C'])
                elif i2 == 'D':
                    self.WaitClickXPATH(dict['D'])
                elif i2 == 'E':
                    self.WaitClickXPATH(dict['D'])
                elif i2 == 'F':
                    self.WaitClickXPATH(dict['F'])
                time.sleep(random.uniform(0.2, 0.4))
            time.sleep(random.randint(1, 2))
            # self.WaitClickXPATH(dict['confirm'])
            self.WaitClickCSS(dict['confirm'])

        print('答题完成')

    def open_driver_gui(self, user):
        print(user)
        self.driver.get(value.url)
        self.driver.set_window_size('640', '960')
        time.sleep(random.randrange(1, 3))
        self.driver.find_element_by_id('email').send_keys(user)
        time.sleep(random.randrange(1, 3))
        self.driver.find_element_by_id('password').send_keys(user[-6:])
        time.sleep(random.randrange(1, 3))
        self.driver.find_element_by_id('login-submit').click()
        time.sleep(random.randrange(3, 5))
        self.WaitClickXPATH(xpath.mryt)
        time.sleep(random.randrange(2, 4))

    def Response_GUI(self, type):
        if type == 'wx':
            dict = xpath.wx
        elif type == 'lx':
            dict = xpath.lx
        print('--------------------')
        self.WaitClickXPATH(dict['place'])
        # num = random.randint(2, 3)
        num = 50

        # self.CheckTxt(xpath.hqz, value.hqz, TF=False)
        # num = int(self.GetTxt(dict['count']))
        # print(num)
        for j in range(num):
            self.CheckTxt(xpath.hqz, value.hqz, TF=False)
            j = j + 1
            print('第%i题：'%j)
            time.sleep(1)
            # 进入答题模块，获取答案，选择答案
            self.Reply(dict)
            # 如果是最后一题，页面返回，否则，下一题
            time.sleep(random.uniform(1, 3))
            if j == num:
                self.driver.close()
                pass
            else:
                self.WaitClickXPATH(dict['next'])
            print('共%i题第%i题回答完毕。'% (num, j))
            time.sleep(random.uniform(0.2, 0.4))

        def Get_Tklist(self, user):
            self.open_driver_gui(user=user)
            tklist = self.GetList(xpath.tklist)
            return tklist

        def Goto_tk(self, kind):
            tklist = xpath.tklist
            print(tklist)
            print(kind)
            str = tklist[:-2] + '[' + kind + ']' + tklist[-2:]
            print(str)
            self.WaitClickXPATH(str)


if __name__ == '__main__':
        firefox = conf.get('conf', 'firefox')
        geckodriver = conf.get('conf', 'geckodriver')
        headers = {'host': 'www.shoujitiku.net', 'connection': 'keep-alive',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
                   'accept-encoding': 'gzip, deflate', 'accept-language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
                   'cookie': 'ASP.NET_SessionId=khhcccxxdq1lfnrewhu5lo5h; LoginUserKey=13C2C1A702AE2DE0CCB9ECA772FDB96D88F7F3FFDFD154840102E48006AD0CA9C07ADB5BEF761DC5553B8115741BB7F963245D18DC35035342F125785E94DB62D32C8C889A586CC9947B77798DB7B89AA25462ECA90FA6F27BA76DFBDA27218B4CF4050FE84530F8772A33FBBA7015B2DD79CD79D589C3592748B520EDEE622A70D1D1E1F94F2CD4B771A3A7036EE1027AAA0A99FFDB57D405207202DF0C9BECA8AB2BD0C33A5BC8E754913BDB6B8347E1B4D402962A6902479D15C2F0B12F21D2E8F9AD1EE6886714E6CEA2AE3E9BF4DA632460BF4317B224B737D614BB2A268855CB08014920BFF8050609C9165BC94C7D7029643DF30D94F14A0A19DBAD7E73735E0219142EAA1BBAABADDAE18EE79D86885DFB5DAA641F4BD64E34B3476245777C09C2985F8ABB7F2FF10E106CD72AE0396094DA2115E4FBC005EBE9F2611108518EDFECF24D491783FCEE668784E8CC3206F7AEEB318668D46C6B49FC428388CD5FC65F65ABDDB50CF1EDA8783EF9E44F7D89437FEA6DB86F2C10317B357FE308714DA03AEB8839CC32A936AAEF9FC3D63EBFABFD8428ED2223E56CE43EF0A9F0AEBDFCAED4CBE6FB1F5CB89AE7450C3BA1A9D5BFEF9A544FF47D67E9FD1C6759D47778606A1A306358394BE656BE5AB50E73F94DB0E8687270912B46079A78FECBA6DE07302A74929A0841B29F1EE1A4606AAB645161ACF0BC84AF0EF38AD280F3F8983DB9799D71FF094732B0EE01E6E17BFAD9D0C39E158D73214CFA'
                   }
        ethernet_url = 'http://www.shoujitiku.net/YT_WeiXin/Login'

        rebot = answerBot(
            geckodriver_dir=geckodriver,
            firefox_dir=firefox,
            uri='/YT_WeiXin/Default?oid=ouKFYs-jgAY6iY0W-EV4X8D5y4Yk',
            **headers
        )
        rebot.Response_GUI(type='wx')
        time.sleep(5)
