# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-01-21 2:23
# @Author  : Jackadam
# @Email   :
# @File    : Thread_work.py
# @Software: PyCharm
# 检查配置文件，检查配套程序，检查网络的类，作为子线程
from tools.answerBot import *
from tools.sniffer import *
from tools.check import *
from PyQt5.QtCore import QThread, pyqtSignal, QRunnable, QThreadPool


# 各种自检的部分，检查配置文件，检查软件位置，检查网络^………………
class CheckThread(QThread):
    # 定义一个信号
    uptext = pyqtSignal(str)
    # 定义另一个信号
    enable_B = pyqtSignal(str)
    url = ''

    def __init__(self):
        # 初始化函数，默认
        super(CheckThread, self).__init__()

    def run(self):
        # 检查配置文件是否存在
        section = check_conf()
        # print(section)
        if section == True:
            msg = '配置文件存在'
            self.uptext.emit(msg)
            msg = '更新配置文件'
            self.uptext.emit(msg)
            make_conf('up')
        else:
            msg = '配置文件不存在'
            self.uptext.emit(msg)
            msg = make_conf()
            if msg == True:
                msg = '配置文件创建完成'
            self.uptext.emit(msg)
        msg = '读取配置文件'
        self.uptext.emit(msg)
        files = read_conf()
        self.firefox_dir = files.get('firefox')
        self.geckodriver_dir = files.get('geckodriver')
        self.wechat_dir = files.get('wechat')
        self.npcap_dir = files.get('npcap')
        self.internet_host = files.get('internet')
        self.winpcap_dir = files.get('winpcap')
        self.notfound='notfound'
        print('关键代码')
        print(files)
        print(self.firefox_dir)
        print(type(self.firefox_dir))
        print(self.geckodriver_dir)
        print(self.wechat_dir)
        print(self.npcap_dir)
        print(self.winpcap_dir)
        print(type(self.winpcap_dir))
        print(self.notfound)
        print(type(self.notfound))
        print('--------------')
        if self.firefox_dir != 'notfound':
            self.uptext.emit('火狐通过自检')
        else:
            self.uptext.emit('火狐没有通过自检，请安装火狐。')
            self.uptext.emit('并确保安装在C盘或D盘默认目录下')
            self.uptext.emit('安装时仅更改盘符。')
            self.enable_B.emit('firefox')
        #
        #
        if self.geckodriver_dir != 'notfound':
            self.uptext.emit('驱动通过自检')
        else:
            self.uptext.emit('驱动没有通过自检，请安装驱动。')
            self.uptext.emit('并确保安装在C盘或D盘默认目录下')
            self.uptext.emit('安装时仅更改盘符。')
            self.enable_B.emit('geckodriver')
        #
        #
        if self.wechat_dir != 'notfound':
            self.uptext.emit('微信通过自检')
        else:
            self.uptext.emit('微信没有通过自检，请安装驱动。')
            self.uptext.emit('并确保安装在C盘或D盘默认目录下')
            self.uptext.emit('安装时仅更改盘符。')
            self.enable_B.emit('wechat')

        #
        if self.winpcap_dir == 'notfound'  and self.winpcap_dir == 'notfound':
            self.uptext.emit('破解工具通过自检')
        else:
            self.uptext.emit('破解工具没有通过自检，请安装驱动。')
            self.uptext.emit('并确保安装在C盘或D盘默认目录下')
            self.uptext.emit('安装时仅更改盘符。')
            self.enable_B.emit('npcap')
        self.uptext.emit('配置检查结束')
        #
        #
        if check_net(self.internet_host):
            # self.enable_B.emit('internet')
            self.enable_B.emit('uid')
            self.uptext.emit(self.internet_host + '连接成功')

        else:
            self.uptext.emit(self.internet_host + '连接失败')
        if check_net(self.url):
            self.enable_B.emit('ethernet')
            self.uptext.emit(self.url + '连接成功')
        else:
            self.uptext.emit(self.url + '连接失败')


# 监听网络，获取request的类，作为子线程
class ListenThread(QThread):
    get_header = pyqtSignal(dict)

    def __init__(self):
        super(ListenThread, self).__init__()

    def run(self):
        print('start listen')
        self.request = sniffer(self.url)
        print(self.request)
        print('end listen')
        dict={
            'uri':self.request.uri,
            'headers':self.request.headers,
        }
        print(dict)
        self.get_header.emit(dict)


class BotThread(QThread):
    enable_B = pyqtSignal(str)
    Add_Combo = pyqtSignal(list)

    def __init__(self, **kwargs):
        super(BotThread, self).__init__()
        self.kw = kwargs
        print('构造开始')
        print(self.kw)

    def run(self):
        print('实例化')
        rebot = answerBot(**self.kw)
        rebot.Response_GUI(type='wx')