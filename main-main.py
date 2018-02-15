import sys
import time
import win32api
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QRunnable, QThreadPool
from mainwindow import Ui_MainWindow
from tools.Thread_work import *
from PyQt5.QtCore import QStringListModel
import webbrowser
from tools.sniffer import *
from tools.answerBot import *


# 定义主窗口的类，继承自UI文件生成的py
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent=parent)
		self.setupUi(self)
		self.textBrowser.append('配置文件读取中，请耐心等待几秒')
		self.B_uid.setEnabled(False)
		self.B_internet.setEnabled(False)
		self.B_ethernet.setEnabled(False)
		
		# 获取url框的地址，解出其中的IP地址，并赋值给子线程类，好让子线程可以检查联通状态
		self.ethernet_url = self.urlEdit.text()
		print(self.ethernet_url)
		print(type(self.ethernet_url))
		if self.ethernet_url != '':
			# print('有')
			urls = self.urlEdit.text().split('/')
			urls = urls[2].split(':')
			self.ethernet_url = urls[0]
		else:
			
			# print('空')
			pass
		
		self.work1 = CheckThread()
		self.work1.start()
		self.work1.enable_B.connect(self.enable_B)
		self.work1.uptext.connect(self.UpText)
		self.work1.quit()
	
	def setHeader(self, bro_dict):
		print('setHeader')
		self.uri = bro_dict.get('uri')
		print(self.uri)
		self.headers = dict(bro_dict.get('headers'))
		print(self.headers['user-agent'])
		self.enable_B('internet')
	
	def UpText(self, str):
		print('UpText.start')
		self.textBrowser.append(str)
	
	def enable_B(self, str):
		if str == 'uid':
			self.B_uid.setEnabled(True)
		elif str == 'internet':
			self.B_internet.setEnabled(True)
		elif str == 'ethernet':
			self.B_ethernet.setEnabled(True)
	
	def add_combo(self, list):
		msgkingbox = QStringListModel()
		self.kindBox.addItems(list)
		self.msgkingbox.addItems(list)
		print(list)
		self.B_ethernet.setEnabled(True)
		pass
	
	def uid(self):
		self.B_uid.setEnabled(False)
		self.textBrowser.append('启动微信:')
		filedir = self.work1.wechat_dir
		print(filedir)
		win32api.ShellExecute(0, 'open', filedir, '', '', 1)
		self.work2 = ListenThread()
		self.work2.url = '/YT_WeiXin/Default?oid='
		self.work2.start()
		self.work2.get_header.connect(self.setHeader)
		self.textBrowser.append('请在微信中进入龙谷公众号，并点击开始答题。')
		
		self.work2.quit()
	
	def internet(self):
		# self.B_internet.setEnabled(False)

		print('internet-----------------------------')
		print(self.work1.geckodriver_dir)
		print(self.work1.firefox_dir)
		print(self.uri)
		print(self.headers)
		print(type(self.headers))
		print('internet-----------------------------')
		self.work3 = BotThread(
			geckodriver_dir=self.work1.geckodriver_dir,
			firefox_dir=self.work1.firefox_dir,
			uri=self.uri,
			**self.headers
		)
		self.work3.start()
	
	def ethernet(self, str):
		self.work3.quit()
		print('work3 start')
		
		self.work3 = BotThread(
			name=self.user.get('name'),
			num=self.user.get('num'),
			kind=self.user.get('kind'),
			geckodriver_dir=self.work1.geckodriver_dir,
			firefox_dir=self.work1.firefox_dir,
			url=self.ethernet_url,
		
		)
		self.work3.enable_B.connect(self.enable_B)
		self.work3.Add_Combo.connect(self.add_combo)
		self.work3.start()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())
