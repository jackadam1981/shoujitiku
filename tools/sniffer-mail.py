import pcap
import dpkt
import json
from tools.my_email import *
def sniffer(tag):
    print('start sniffer')
    pc = pcap.pcap()  #开始捕获数据包
    print('read pcap', tag)
    flag = False     #设定标记为假
    i = 0
    j = 0            #定义两个参数
    for timestamp, buf in pc:   #解析数据包为时间和内容
        i = i + 1
        print(i)
        eth = dpkt.ethernet.Ethernet(buf)        #继续解析内容
        ip = eth.data
        if isinstance(ip.data, dpkt.tcp.TCP):    #如果是标准数据包
            print('t', i, j)          #打印参数
            tcp = ip.data
            print(tcp.data)             #打印数据包内容
            if j==1:
                #这个是在第二行的数据包解析后才执行的。
                #j没有自增，始终为0，如果有值了，那就是需要保留的第二行cookie
                end_add = tcp.data      #取所有这个包的数据为end_add
                flag = True            #设置标记为真
            else:
                try:
                    request = dpkt.http.Request(tcp.data)           #获取数据包中的equest
                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                    continue

                # if request.headers['host'] == tag:
                if tag in request.uri:               #如果目标在request当中的url字段
                    j = 1                            #给j赋值为i
                    re_add = request
        if flag == True:            #如果标记为真，那么就给cookie加上第二行的内容
            print('------------')
            re_add.headers['cookie']=re_add.headers['cookie']+str(end_add)[2:-9]
            print(re_add.headers.get('cookie'))
            print(re_add)
            print('------------')
            return re_add


if __name__ == '__main__':
    print('hello world!')
    request = sniffer('/YT_WeiXin/Default?oid=')
    # request = sniffer('www.google.com')
    print('---------')
    # print('return all ', request)
    # print(type(request))
    print(request.headers)
    print(type(request.headers))

    request.headers['uri']=request.uri
    json_str=json.dumps(request.headers)
    sendmail(json_str)


