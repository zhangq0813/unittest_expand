import emailPerson
import yagmail
'''
self.user = user
self.password = password
self.host = host
self.toemaill = toemaill
self.toemailcc = toemailcc
self.emailsubject = emailsubject
self.emailcontent = emailcontent
'''
user='zhangqiang@yitong.com.cn'
password = '01112358@zhang'
host = 'smtphm.qiye.163.com'
emaillist = ['965928979@qq.com','zhangq0813@163.com']
emailpkg = ["D:\\09-AutoTest\\test.py"]
contentword = ['this is an test_email']
subjects = '主题，自动化测试报告'
report ='D:\\09-AutoTest\\test.py'


yag = yagmail.SMTP(self.user, self.password, self.host)

aa = emailPerson.send_eamil(report)

