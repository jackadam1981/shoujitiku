# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-01-17 14:23
# @Author  : Jackadam
# @Email   :
# @File    : check.py
# @Software: PyCharm
import os, sys, subprocess
from configparser import ConfigParser
import subprocess

# print(os.getcwd())
fp_dir = os.getcwd()
# print(fp_dir)
fp = fp_dir + '\conf.ini'  # 定义配置文件名


def recursive_search_dirs(dirs, target_files):
    """Recursive search directories"""
    """循环搜索目录，调用目录下搜索文件"""
    for d in dirs:
        r = recursive_search(d, target_files)
        if r:
            return r


def recursive_search(path, target_files):
    """Recursively search for files"""
    """目录下搜索文件"""
    for root, _dirs, files in os.walk(path):
        for filename in files:
            if filename in target_files:
                return os.path.join(root, filename)


def get_extension(file_name):
    # A list of all the possible search directories
    # 从列表中搜索指定文件
    dirs = [
        'C:\Program Files',
        'C:\Program Files (x86)',
        'D:\Program Files',
        'D:\Program Files (x86)',
        os.getcwd(),
    ]
    file_dir = recursive_search_dirs(dirs, file_name)
    if file_dir:
        print("Foundin %s" % file_dir)
        return file_dir

    if not file_dir:
        print("not found")
        # sys.exit(1)
        return 'notfound'


def check_conf():
    file = os.path.split(fp)[1]
    files = os.listdir(os.path.split(fp)[0])
    if file not in files:
        return False
    return True


def make_conf(type='make'):
    conf = ConfigParser()  # 实例化
    print('配置文件，创建中')
    tes = open(fp, 'a')
    tes.close()
    firefox = str(get_extension(['firefox.exe']))
    geckodriver = str(get_extension(['geckodriver.exe']))
    WeChat = str(get_extension(['WeChat.exe']))
    npcap = str(get_extension(['NPFInstall.exe']))
    winpcap = str(get_extension(['rpcapd.exe']))

    conf.read(fp)  # 打开conf
    if type != 'up':
        conf.add_section('conf')  # 添加conf节点
    print('add section')
    conf.set('conf', 'internet', 'www.shoujitiku.net')
    conf.set('conf', 'firefox', firefox)  # 添加值
    conf.set('conf', 'geckodriver', geckodriver)  # 添加值
    conf.set('conf', 'wechat', WeChat)  # 添加值
    conf.set('conf', 'npcap', npcap)  # 添加值
    conf.set('conf', 'winpcap', winpcap)  # 添加值

    print('set all', fp)
    with open(fp, 'w') as fw:  # 循环写入
        conf.write(fw)
    return True


def read_conf():
    # print('read')

    files = os.listdir()
    conf = ConfigParser()  # 实例化
    conf.read(fp)  # 打开conf
    print('打开配置文件', fp)
    file_list = {
        'firefox': conf.get('conf', 'firefox'),
        'geckodriver': conf.get('conf', 'geckodriver'),
        'wechat': conf.get('conf', 'wechat'),
        'npcap':conf.get('conf','npcap'),
        'winpcap':conf.get('conf','winpcap'),
        'internet': conf.get('conf', 'internet'),
    }
    print(file_list)
    return file_list


def check_net(str):
    return1 = subprocess.call('ping %s' % str, shell=False)
    if return1:
        return False
    else:
        return True


if __name__ == '__main__':
    if check_conf():
        make_conf('up')
        print('ok')
    else:
        print('bad')
        make_conf('make')
        print(read_conf())
