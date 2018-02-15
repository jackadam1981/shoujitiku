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
		msg = '读取配置文件'
		self.uptext.emit(msg)
		files = read_conf()
		print('read over')
		print(files)
		self.firefox_dir = files.get('firefox')
		self.geckodriver_dir = files.get('geckodriver')
		self.wechat_dir = files.get('wechat')
		self.npcap_dir = files.get('npcap')
		self.internet_host = files.get('internet')
		print(self.firefox_dir)
		print(self.geckodriver_dir)
		print(self.wechat_dir)
		print(self.npcap_dir)
		print(self.internet_host)
		self.uptext.emit('配置文件正确')
		self.uptext.emit('检查网络配置')
		internet_state=check_net(self.internet_host)
		print(internet_state)
		if internet_state==True:
			self.uptext.emit('当前网络为互联网，可以破解答题。')
			

		if self.wechat_dir != 'notfound' and self.firefox_dir != 'notfound' and self.npcap_dir != 'notfound'and internet_state==True:

			self.enable_B.emit('uid')
			


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
		dict = {
			'uri': self.request.uri,
			'headers': self.request.headers,
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
		for i in range(10):
			rebot.Response_GUI(type='wx')
