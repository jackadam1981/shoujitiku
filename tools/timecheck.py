import requests,time

def checktime():
	set_end = (2018,10 , 1, 8, 0, 0, 0, 0, 0)
	end_time = time.mktime(set_end)
	get_now =requests.get('https://now.httpbin.org/').json()['now']['epoch']
	if  get_now>end_time:
		return False
	else:
		return True

if __name__ == '__main__':
    print(checktime())
	