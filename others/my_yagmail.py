import yagmail

yag = yagmail.SMTP(user='zhangq0813@163.com',password ='01112358@zhang',host ='smtp.163.com')
contents1 = ['this is an test_email']
subjects = '主题，自动化测试报告'
#yag.send('965928979@qq.com','zhangq0813@163.com',subject,contents,"d://result.html")
#yag.send(to='965928979@qq.com',cc='zhangq0813@163.com',subject=subjects,contents=contents1) #cc必传
#yag.send(to=(['965928979@qq.com', '894810247@qq.com']),cc='zhangq0813@163.com',subject=subjects,contents=contents1)#cc报错
yag.send(to='965928979@qq.com',cc='zhangq0813@163.com',subject=subjects,contents=contents1\
         ,attachments="D:\\自动化测试\\unittest\\unittest_expand\\test_report\\result.html")  #cc必传
#yag.send(['965928979@qq.com', '894810247@qq.com'], 'zhangq0813@163.com', subjects, contents, "d:\\1.txt")



