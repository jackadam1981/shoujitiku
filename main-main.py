import sys
import time
import win32api
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QRunnable, QThreadPool
from mainwindow import Ui_MainWindow
from tools.Thread_work import *
from tools.timecheck import *

from PyQt5.Qt import QInputDialog

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
		
		# # 获取url框的地址，解出其中的IP地址，并赋值给子线程类，好让子线程可以检查联通状态
		# self.ethernet_url = self.urlEdit.text()
		# print(self.ethernet_url)
		# print(type(self.ethernet_url))
		# if self.ethernet_url != '':
		# 	# print('有')
		# 	urls = self.urlEdit.text().split('/')
		# 	urls = urls[2].split(':')
		# 	self.ethernet_url = urls[0]
		# else:
		#
		# 	# print('空')
		# 	pass
		
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
		self.textBrowser.append(str)
	
	def enable_B(self, str):
		if str == 'uid':
			self.B_uid.setEnabled(True)
		elif str == 'internet':
			if checktime():
				self.B_internet.setEnabled(True)
			else:
				self.UpText('十五都过完了，该更新了。请访问 http://longgu.ml寻找新版本')
		elif str == 'ethernet':
			self.B_ethernet.setEnabled(True)
	
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
			type='internet',
			geckodriver_dir=self.work1.geckodriver_dir,
			firefox_dir=self.work1.firefox_dir,
			uri=self.uri,
			**self.headers
		)
		self.work3.run_internet()
	
	def listmsg(self,tklist):
		my_str,ok=QInputDialog.getItem(self,'选择工种','请选择工种',tklist)
		print(my_str)
		num=tklist.index(my_str)
		print(num)
		self.work3.kind=num
		print(self.work3.kind)
		print('--------------------------------------------------------')
		
	def ethernet(self, str):
		num = self.numEdit.text()
		url = self.urlEdit.text()

		if num == '' or url == '':
			print('请输入')
			self.UpText('请输入内部答题地址和身份证号。')
		else:
			print(num)
			print(url)
			self.work3 = BotThread(
				type='ethernet',
				num=num,
				url=url,
				geckodriver_dir=self.work1.geckodriver_dir,
				firefox_dir=self.work1.firefox_dir,
			)
			self.work3.enable_B.connect(self.enable_B)
			self.work3.add_listmsg.connect(self.listmsg)
			self.work3.run_ethernet()
			print('------------')
			print(self.work3.kind)
			self.work3.Goto_tk(self.work3.kind)
			self.work3.Response()


		
	
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())
