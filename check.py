import os
import sys
import time
from PyQt5 import QtWidgets
from checkgui import Ui_MainWindow
from tools.sys_check import CheckThread
import webbrowser


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent=parent)
		self.setupUi(self)
		self.B_wechat.setEnabled(False)
		self.B_firefox.setEnabled(False)
		self.B_npcap.setEnabled(False)
		self.B_start.setEnabled(False)
		
		self.check = CheckThread()
		self.check.uptext.connect(self.Add_Text)
		self.check.enable_B.connect(self.Enable_Button)
		self.check.start()
	
	def Add_Text(self, str):
		# self.textBrowser.append(str)
		self.textBrowser.insertPlainText(str + '\n')
	
	def Enable_Button(self, str):
		if str == 'wechat':
			self.B_wechat.setEnabled(True)
			pass
		elif str == 'firefox':
			self.B_firefox.setEnabled(True)
			pass
		elif str == 'npcap':
			self.B_npcap.setEnabled(True)
			pass
		elif str == 'start':
			self.B_start.setEnabled(True)
			pass
		else:
			pass
	
	def wechat(self):
		webbrowser.open_new('http://dldir1.qq.com/weixin/Windows/WeChatSetup.exe')
	
	def firefox(self):
		webbrowser.open_new(
			'https://download-ssl.firefox.com.cn/releases-sha2/full/58.0/zh-CN/Firefox-full-latest-win64.exe')
	
	def npcap(self):
		print('npcap')
		webbrowser.open_new(
			'https://nmap.org/npcap/dist/npcap-0.98.exe'
		)
	
	def startdtj(self):
		print('启动答题机')
		os.system('main-main.exe')
		w.close()
		pass


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())
