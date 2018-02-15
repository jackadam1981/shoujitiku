from PyQt5.QtCore import QThread, pyqtSignal
from tools.check import *


class CheckThread(QThread):
	# 定义一个信号
	uptext = pyqtSignal(str)
	# 定义另一个信号
	enable_B = pyqtSignal(str)
	
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
		
		if  self.wechat_dir != 'notfound':
			self.uptext.emit('微信通过自检')
			self.uptext.emit(self.wechat_dir)
		else:
			self.uptext.emit('微信没有通过自检，请安装驱动。')
			self.uptext.emit('并确保安装在C盘或D盘默认目录下')
			self.uptext.emit('安装时仅更改盘符。')
			self.enable_B.emit('wechat')
		
		if  self.firefox_dir != 'notfound':
			self.uptext.emit('火狐通过自检')
			self.uptext.emit(self.firefox_dir)
		else:
			self.uptext.emit('火狐没有通过自检，请安装火狐。')
			self.uptext.emit('并确保安装在C盘或D盘默认目录下')
			self.uptext.emit('安装时仅更改盘符。')
			self.enable_B.emit('firefox')
		
		if  self.npcap_dir != 'notfound':
			self.uptext.emit('破解工具通过自检')
			self.uptext.emit(self.npcap_dir)
		else:
			self.uptext.emit('破解工具没有通过自检，请安装驱动。')
			self.uptext.emit('并确保安装在C盘或D盘默认目录下')
			self.uptext.emit('安装时仅更改盘符。')
			self.enable_B.emit('npcap')
		self.uptext.emit('配置检查结束')
		
		if self.wechat_dir != 'notfound' and self.firefox_dir != 'notfound' and self.npcap_dir != 'notfound':
			self.enable_B.emit('start')
if __name__ == '__main__':
    tt=CheckThread()
    tt.run()