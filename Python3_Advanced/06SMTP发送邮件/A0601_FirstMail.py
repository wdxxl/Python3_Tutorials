
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from getpass import getpass

# 第三方SMTP服务
mail_host = "smtp.qq.com"
mail_user = "455142495@qq.com"

sender = "455142495@qq.com"
receivers = ['455142495@qq.com']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header('菜鸟教程', 'utf-8')
message['To'] = Header('测试', 'utf-8')


subject = "Python SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    password = getpass("Password: ")
    smtpObj.login(mail_user, password)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")