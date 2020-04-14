###待调试IndentationError: expected an indented block

import yagmail

class emailSend:

def __init__(self,user,password,host,toemaill,toemailcc,emailsubject,emailcontent):
    self.user = user
    self.password = password
    self.host = host
    self.toemaill = toemaill
    self.toemailcc = toemailcc
    self.emailsubject = emailsubject
    self.emailcontent = emailcontent

def send_eamil(report):
    """自定义封装发送邮件方法"""
    #yag = yagmail.SMTP(user='zhangq0813@163.com',password ='01112358@zhang',host ='smtp.163.com')
    emailpkg = report
    yag = yagmail.SMTP(self.user, self.password, self.host)
    yag.send(to=self.toemaill, cc=self.toemailcc, subject=self.emailsubject, contents=self.emailcontent,\
             attachments=emailpkg)

 #print("the test email has send out !")
