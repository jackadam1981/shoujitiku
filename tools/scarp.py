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


class scarp(object):
    def __init__(self, *args, **kwargs):
        print(kwargs)
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", kwargs.get('user-agent'))
        self.driver = webdriver.Firefox(
            firefox_binary=kwargs.get('firefox_dir'),
            executable_path=kwargs.get('geckodriver_dir'),
            firefox_profile=profile,
        )
        print(len(kwargs.get('cookie')))
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
        print('click', str)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, str))).click()

    def WaitClickCSS(self, str):
        print('click', str)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, str))).click()

    def CheckTxt(self, str1, str2, time=10, TF=True):
        if TF == True:
            print('true')
            WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element((By.XPATH, str1), str2))
        else:
            print('flase')
            WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element((By.XPATH, str1), str2))

    # 获取文字,因为排行榜会有空排名，所以try一下，
    def GetTxt(self, str):
        try:
            text = WebDriverWait(self.driver, 30).until(EC.visibility_of(self.driver.find_element_by_xpath(str))).text
            return text
        except:
            return 0
            # 获取文字,因为排行榜会有空排名，所以try一下，

    def GetList(self, str):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of(self.driver.find_element_by_xpath(str)))
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
        print('题目长度%i,等待%i' % (len(question), 0.06 * len(question)))
        answer_type = question[1:4]
        print(answer_type)
        answertext = (self.GetAnswer())
        # # js = 'document.getElementById("stdaan").style.display = "block"'
        # # #js = ' $("#stdaan").show();'
        # # driver.execute_script(js)
        print('正确答案： %s      ' % answertext, end='')
        sys.stdout.flush()
        #
        time.sleep(0.06 * len(question))
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

    def Response_GUI(self,type):
        if type =='wx':
            dict=xpath.wx
        elif type == 'lx':
            dict =xpath.lx
        print('--------------------')
        self.WaitClickXPATH(dict['place'])
        # num = random.randint(2, 3)
        num = 4

        # self.CheckTxt(xpath.hqz, value.hqz, TF=False)
        # num = int(self.GetTxt(xpath.lx['count']))
        print(num)
        for j in range(num):
            self.CheckTxt(xpath.hqz, value.hqz, TF=False)
            j = j + 1
            print(j)
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
            print('第%i题回答完毕。' % j)
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


#
if __name__ == '__main__':
    firefox = conf.get('conf', 'firefox')
    geckodriver = conf.get('conf', 'geckodriver')
    headers = {'host': 'www.shoujitiku.net', 'connection': 'keep-alive',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
               'accept-encoding': 'gzip, deflate', 'accept-language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
               'cookie': 'ASP.NET_SessionId=bex50kx5hv4tldt044evjomt; LoginUserKey=13C2C1A702AE2DE0CCB9ECA772FDB96D88F7F3FFDFD154840102E48006AD0CA9C07ADB5BEF761DC5553B8115741BB7F963245D18DC35035342F125785E94DB62D32C8C889A586CC9947B77798DB7B89AA25462ECA90FA6F27BA76DFBDA27218B4CF4050FE84530F8772A33FBBA7015B2DD79CD79D589C3592748B520EDEE622A70D1D1E1F94F2CD4B771A3A7036EE1027AAA0A99FFDB57D405207202DF0C9BECA8AB2BD0C33A5BC8E754913BDB6B8347E1B4D402962A6902479D15C2F0B12F21B4144A5F11E9F2350F654D96601325ACD15FD54CBB49A9A46B76D560780659874695B600F7704B8819D9AD80B7CD66B55A3992113C7D8D255C3A943411330FB475C036FCB1ABF9F1BB2DCD927AB405E15EE895AB76AD3BB7F90A0FB2AA026F22FA183AC29EDEFE22C057F81FFE14DED0D9C9263A75ECC020F750005E71C46BA4B1320FBEA960738DF6930370E60E9DB95BFB8E9657F096073DBC14E4F64ADA710C5BA294E4E88840A9A5ECCFEC28DA1C2A89D548DFC8C80B16B5134603B34744D15846CF5F82E3BA1E5AC0254877514381B111782AC9FA0D2163DD069AC3D85715C12CB31254DB41F63F18159AD243079459E0E1ACCFE726B6BFC594DD1D3CF59E4670557312069947937BF370FC16C78B52CB06112BEE837992987DC1FAB27D8C9C6A4EB601898859AFA1077545485A26E940829046612D74F8235D2259FF6C2325CE0DCFEAA56BB9B6DF640514BD454B39981C89D157AADC425AB834D39455'}

    ethernet_url = 'http://www.shoujitiku.net/YT_WeiXin/Login'

    rebot = scarp(
        geckodriver_dir=geckodriver,
        firefox_dir=firefox,
        uri='/YT_WeiXin/Default?oid=ouKFYs-jgAY6iY0W-EV4X8D5y4Yk',
        **headers
    )
    rebot.Response_GUI(type='wx')
    time.sleep(5)
