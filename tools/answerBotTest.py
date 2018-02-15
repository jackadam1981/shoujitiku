import os
from configparser import ConfigParser
from tools.answerBot import *

fp_dir = os.getcwd()
fp = fp_dir + '\conf.ini'  # 定义配置文件名
conf = ConfigParser()  # 实例化
conf.read(fp)  # 打开conf

if __name__ == '__main__':
    firefox = conf.get('conf', 'firefox')
    geckodriver = conf.get('conf', 'geckodriver')
    headers = {'host': 'www.shoujitiku.net', 'connection': 'keep-alive',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
               'accept-encoding': 'gzip, deflate', 'accept-language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
               'cookie': 'ASP.NET_SessionId=888888888888888; stCode=888888888888888888; LoginUserKey=88888888888'}
    ethernet_url = 'http://www.shoujitiku.net/YT_WeiXin/Login'

    rebot = answerBot(
        geckodriver_dir=geckodriver,
        firefox_dir=firefox,
        uri='/YT_WeiXin/Default?oid=8888888888888888888888',
        **headers
    )
    for i in range(10):
        rebot.Response_GUI(type='wx')
        time.sleep(5)