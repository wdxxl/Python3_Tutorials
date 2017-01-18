
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from getpass import getpass

# 第三方SMTP服务
mail_host = "smtp.qq.com"
mail_user = "455142495@qq.com"

sender = "455142495@qq.com"
receivers = ['455142495@qq.com']

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header('菜鸟教程', 'utf-8')
message['To'] = Header('测试', 'utf-8')
subject = "Python SMTP Attachments 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

mail_msg = '''
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com" target="_blank">菜鸟教程连接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
'''

msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

# 指定图片为当前目录
fp = open("overview.png","rb")
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片ID，在HTML文件中引用
msgImage.add_header("Content-ID", "<image1>")
message.attach(msgImage)

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    password = getpass("Password: ")
    smtpObj.login(mail_user, password)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
