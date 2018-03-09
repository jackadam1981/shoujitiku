from selenium import  webdriver
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.get_screenshot_as_file('test.png')
print(driver.title)
driver.close()

