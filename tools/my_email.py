from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


from_addr = 'jackadam@163.com'
password = 'lq83XrpOxso0ghkM'
to_addr = 'jackadam@sina.com'
smtp_server = 'smtp.163.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendmail(message):
    print(message)
    msg = MIMEText(message, 'plain', 'utf-8')

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header('sniffer mail', 'utf-8').encode()

    print(msg)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

if __name__ == '__main__':
    sendmail('hello')

