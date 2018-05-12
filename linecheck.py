# -*- coding: utf-8 -*-
#coding by zk
import codecs
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib
import time
logtime = time.strftime('%Y%m%d',time.localtime(time.time()))
#打开当日生成的线路检查的log日志文件
f=codecs.open('C:/LineCheck/log/xxx.xx.xx.xx-' + logtime + '.log','r','utf-8')
#读取内容并赋值给变量
s=f.readlines()
f.flush()
f.close()
#循环检查读取的检查日志中是否存在字符“down”
for fileLine in s:
    #如果存在down，说明有异常，则发送异常告警邮件
    if u'down' in fileLine:

        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))
        from_addr ='发件邮箱地址'
        password = '发件邮箱密码'
        to_addr = '收件地址'
        cc_addr = '抄送地址'
        smtp_server = '邮件服务器地址'
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Cc'] = cc_addr
        msg['Subject'] = Header(u'IP电话线路检查异常告警-xxx.xx.xx.xx', 'utf-8').encode()
        # add MIMEText:
        msg.attach(MIMEText( u'xxx.xx.xx.xx线路检查存在异常！', 'plain', 'utf-8'))
        # add file:
        with open("C:\\LineCheck\\log\\xxx.xx.xx.xx-" + logtime + ".log", 'rb') as f:
             mime = MIMEBase('text', 'log', filename="xxx.xx.xx.xx-" + logtime + ".log")
             mime.add_header('Content-Disposition', 'attachment', filename="xxx.xx.xx.xx-" + logtime + ".log")
             mime.add_header('Content-ID', '<0>')
             mime.add_header('X-Attachment-Id', '0')
             mime.set_payload(f.read())
             encoders.encode_base64(mime)
             msg.attach(mime)
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr,[to_addr]+[cc_addr], msg.as_string())
        server.quit()
        break
    else:
      #如果不存在down，则说明正常，则发送正常通知邮件
        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))
        from_addr ='发件邮箱地址'
        password = '发件邮箱密码'
        to_addr = '收件地址'
        cc_addr = '抄送地址'
        smtp_server = '邮件服务器地址'
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Cc'] = cc_addr
        msg['Subject'] = Header(u'IP电话线路检查正常通知-...', 'utf-8').encode()
        # add MIMEText:
        msg.attach(MIMEText( u'...线路检查正常！', 'plain', 'utf-8'))
        # add file:
        with open("C:\\LineCheck\\log\\...-" + logtime + ".log", 'rb') as f:
             mime = MIMEBase('text', 'log', filename="...-" + logtime + ".log")
             mime.add_header('Content-Disposition', 'attachment', filename="...-" + logtime + ".log")
             mime.add_header('Content-ID', '<0>')
             mime.add_header('X-Attachment-Id', '0')
             mime.set_payload(f.read())
             encoders.encode_base64(mime)
             msg.attach(mime)
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr,[to_addr]+[cc_addr], msg.as_string())
        server.quit()
        break

#以下原理同上

logtime = time.strftime('%Y%m%d',time.localtime(time.time()))
f=codecs.open('C:/LineCheck/log/...-' + logtime + '.log','r','utf-8')
s=f.readlines()
f.flush()
f.close()

for fileLine in s:
    if u'down' in fileLine:

        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))
        from_addr =''
        password = ''
        to_addr = ''
        cc_addr = ''
        smtp_server = ''
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Cc'] = cc_addr
        msg['Subject'] = Header(u'IP电话线路检查异常告警-...', 'utf-8').encode()
        # add MIMEText:
        msg.attach(MIMEText( u'...', 'plain', 'utf-8'))
        # add file:
        with open("C:\\LineCheck\\log\\...-" + logtime + ".log", 'rb') as f:
             mime = MIMEBase('text', 'log', filename="...-" + logtime + ".log")
             mime.add_header('Content-Disposition', 'attachment', filename="...-" + logtime + ".log")
             mime.add_header('Content-ID', '<0>')
             mime.add_header('X-Attachment-Id', '0')
             mime.set_payload(f.read())
             encoders.encode_base64(mime)
             msg.attach(mime)
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr,[to_addr]+[cc_addr], msg.as_string())
        server.quit()
        break
    else:

        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))
        from_addr =''
        password = ''
        to_addr = ''
        cc_addr = ''
        smtp_server = 'mail.unionpay.com'
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Cc'] = cc_addr
        msg['Subject'] = Header(u'IP电话线路检查正常通知-...', 'utf-8').encode()
        # add MIMEText:
        msg.attach(MIMEText( u'...线路检查正常！', 'plain', 'utf-8'))
        # add file:
        with open("C:\\LineCheck\\log\\...-" + logtime + ".log", 'rb') as f:
             mime = MIMEBase('text', 'log', filename="...-" + logtime + ".log")
             mime.add_header('Content-Disposition', 'attachment', filename="...-" + logtime + ".log")
             mime.add_header('Content-ID', '<0>')
             mime.add_header('X-Attachment-Id', '0')
             mime.set_payload(f.read())
             encoders.encode_base64(mime)
             msg.attach(mime)
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr,[to_addr]+[cc_addr], msg.as_string())
        server.quit()
        break
