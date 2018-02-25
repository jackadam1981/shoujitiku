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
		self.ethernet_host=files.get('ethernet')
		print(self.firefox_dir)
		print(self.geckodriver_dir)
		print(self.wechat_dir)
		print(self.npcap_dir)
		print(self.internet_host)
		print(self.ethernet_host)
		self.uptext.emit('配置文件正确')
		self.uptext.emit('检查网络配置')
		internet_state=check_net(self.internet_host)
		print(internet_state)
		if internet_state==True:
			self.uptext.emit('当前网络为互联网，可以破解答题。')
			
		if self.wechat_dir != 'notfound' and self.firefox_dir != 'notfound' and self.npcap_dir != 'notfound'and internet_state==True:
			self.enable_B.emit('uid')
		print(self.ethernet_host)
		ethernt_state=check_net(self.ethernet_host)
		print(ethernt_state)
		if ethernt_state==True:
			self.uptext.emit('当前网络为铁路网，可以进行内部练习。')
		if  self.firefox_dir != 'notfound' and ethernt_state==True:
			self.enable_B.emit('ethernet')


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
	add_listmsg=pyqtSignal(list)
	kind=''
	def __init__(self, **kwargs):
		super(BotThread, self).__init__()
		self.kw = kwargs
		print('构造开始')
		print(self.kw)
		print('构造结束')
	def run_ethernet(self):
		print('实例化')
		self.rebot = answerBot(**self.kw)
		print('实例化完成')
		tklist=self.rebot.Get_Tklist()
		print(tklist)
		print(type(tklist))
		newlist=[]
		for i in tklist:
			newlist.append(i.text)
		self.add_listmsg.emit(newlist)
		
		
		# rebot.Response_GUI()
		# for i in range(10):
		# 	rebot.Response_GUI()
	def run_internet(self):
		print('实例化')
		self.rebot = answerBot(**self.kw)
		self.rebot.Response_GUI()
		# for i in range(10):
		# 	rebot.Response_GUI()
	def Response(self):
		self.rebot.Response_GUI()
	def Goto_tk(self,kind):
		
		self.rebot.Goto_tk(kind)
		
