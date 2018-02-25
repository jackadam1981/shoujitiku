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


class answerBot(object):
	def __init__(self, *args, **kwargs):
		print('answerBot')
		print(kwargs)
		self.net_type = kwargs.get('type')
		print(self.net_type)
		if self.net_type == 'internet':
			# firefox
			profile = webdriver.FirefoxProfile()
			profile.set_preference("general.useragent.override", kwargs.get('user-agent'))
			self.driver = webdriver.Firefox(
				firefox_binary=kwargs.get('firefox_dir'),
				executable_path=kwargs.get('geckodriver_dir'),
				firefox_profile=profile,
			)
			# chrome
			# options = webdriver.ChromeOptions()
			# options.add_argument('user-agent=' + kwargs.get('user-agent'))
			# self.driver = webdriver.Chrome(options=options)
			
			# print(len(kwargs.get('cookie')))
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
		elif self.net_type == 'ethernet':
			print('ethernet')
			print(kwargs)
			self.driver = webdriver.Firefox(
				firefox_binary=kwargs.get('firefox_dir'),
				executable_path=kwargs.get('geckodriver_dir'),
			)
			if kwargs.get('url')[:4] != 'http':
				url = 'http://' + kwargs.get('url')
			else:
				url = kwargs.get('url')
			
			self.driver.get(url)
			self.driver.set_window_size('640', '960')
			time.sleep(random.randrange(1, 3))
			self.driver.find_element_by_id('email').send_keys(kwargs.get('num'))
			time.sleep(random.randrange(1, 3))
			self.driver.find_element_by_id('password').send_keys(kwargs.get('num')[-6:])
			time.sleep(random.randrange(1, 3))
			self.driver.find_element_by_id('login-submit').click()
			time.sleep(random.randrange(3, 5))
			self.WaitClickXPATH(xpath.mryt)
			time.sleep(random.randrange(2, 4))
	
	def __del__(self):
		self.driver.quit()
	
	def WaitClickXPATH(self, str):
		# print('click', str)
		WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, str))).click()
	
	def WaitClickCSS(self, str):
		# print('click', str)
		WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, str))).click()
	
	def CheckTxt(self, str1, str2, time=60, TF=True):
		if TF == True:
			
			WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element((By.XPATH, str1), str2))
		else:
			
			WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element((By.XPATH, str1), str2))
	
	# 获取文字,因为排行榜会有空排名，所以try一下，
	def GetTxt(self, str):
		try:
			time.sleep(2)
			text = WebDriverWait(self.driver, 60).until(
				EC.visibility_of(self.driver.find_element_by_xpath(str))).text
			return text
		except:
			print('no question')
			return 0
	
	# 获取文字,因为排行榜会有空排名，所以try一下，
	
	def GetList(self, str):
		print('get list1')
		try:
			print('try')
			WebDriverWait(self.driver, 60).until(EC.visibility_of(self.driver.find_element_by_xpath(str)))
			print('wait end')
			list = self.driver.find_elements_by_xpath(str)
			print('get list')
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
				# 设定答案是AB，选另一个答案
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
				ans = str(ans).replace("'", '').replace('[', '').replace(']', '').replace(',', '').replace(' ',
				                                                                                           '')
				daan = "".join((lambda x: (x.sort(), x)[1])(list(ans)))
			else:
				print('题目类型错误？')
				daan = txt
			return daan
	
	# 根据答案回答问题
	def Reply(self, dict=xpath.lx):
		# print('Reply')
		question = self.GetTxt(dict['question'])
		print(question)
		if question != 0:
			print('题目长度%i,等待%i' % (len(question), 0.06 * len(question)))
			answer_type = question[1:4]
			print(answer_type)
			time.sleep(0.06 * len(question))
		else:
			time.sleep(random.randint(3, 6))
		answertext = (self.GetAnswer())
		# # js = 'document.getElementById("stdaan").style.display = "block"'
		# # #js = ' $("#stdaan").show();'
		# # driver.execute_script(js)
		print('正确答案： %s      ' % answertext, end='')
		sys.stdout.flush()
		#
		
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
		self.Get_Tklist()
	
	def Response_GUI(self):
		print('--------------------')
		print(self.net_type)
		
		if self.net_type == 'internet':
			dict = xpath.wx
			self.WaitClickXPATH(dict['place'])
		elif self.net_type == 'ethernet':
			dict = xpath.lx
		print(dict)
		print('--------------------')
		
		
		self.CheckTxt(xpath.hqz, value.hqz, TF=False)
		# num = random.randint(50, 65)
		# num = 50
		num = int(self.GetTxt(dict['count']))
		# print(num)
		i, next_rest, next_rest_time = (0, random.randrange(12, 20),
		                                random.randrange(5, 10))
		for j in range(num):
			self.CheckTxt(xpath.hqz, value.hqz, TF=False)
			j = j + 1
			print('共%i题第%i题' % (num, j))
			time.sleep(1)
			# 进入答题模块，获取答案，选择答案
			self.Reply(dict)
			# 如果是最后一题，页面返回，否则，下一题
			time.sleep(random.uniform(1, 3))
			
			if j == num:
				self.driver.back()
				pass
			else:
				self.WaitClickXPATH(dict['next'])
			print('共%i题第%i题回答完毕。' % (num, j))
			i += 1
			if i == next_rest:
				print('已经连续答了 {} 题，休息 {}秒'.format(i, next_rest_time))
				for j in range(next_rest_time):
					sys.stdout.write('\r程序将在 {}秒后继续答题'.format(next_rest_time - j))
					sys.stdout.flush()
					time.sleep(1)
				print('\n继续')
				i, next_rest, next_rest_time = (0, random.randrange(10, 20),
				                                random.randrange(5, 10))
			time.sleep(random.uniform(0.2, 0.4))
	
	def Get_Tklist(self):
		tklist = self.GetList(xpath.tklist)
		print(tklist)
		return tklist
	
	def Goto_tk(self, kind):
		print('goto tk')
		tklist = xpath.tklist
		print(tklist)
		print(type(tklist))
		
		kind = kind + 1
		kind=str(kind)
		tag = tklist[:-2] + '[' + kind + ']' + tklist[-2:]
		print(tag)
		self.WaitClickXPATH(tag)
