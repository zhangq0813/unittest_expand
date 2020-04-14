import unittest
from test_classpkg.HTMLTestRunner import HTMLTestRunner
import time
import yagmail
#如果创建测试用例套件得话需要导入对应用例得类库
#no such test method in <class 'test_case.test_baidu_date_ddt.TestBaidu'>: test_search3  ->测试套件报错
from test_case.test_baiduPage import TestBaiduPage
from test_case.test_baidu_date_ddt import TestBaidu


def send_eamil(report):
    """自定义封装发送邮件方法"""
    #yag = yagmail.SMTP(user='zhangq0813@163.com',password ='01112358@zhang',host ='smtp.163.com')
    yag = yagmail.SMTP(user='zhangqiang@yitong.com.cn', password='01112358@zhang', host='smtphm.qiye.163.com')
    emaillist = ['965928979@qq.com','zhangq0813@163.com']
    #emailpkg = [report,"D:\\09-AutoTest\\test.py"]
    contentword = ['this is an test_email']
    subjects = '主题，自动化测试报告'
    emailcclist =['zhangq0813@163.com']
    #yag.send(to='965928979@qq.com', cc='zhangq0813@163.com',subject=subjects, contents=contentword,attachments=report)
    #yag.send(to=emaillist, cc='zhangq0813@163.com', subject=subjects, contents=contentword, attachments=report)
    #1、带list发送2、附件绝对路径3、参数必须要用=，4、cc是必传得，那么yagmai.SMTP还有何用处这是4个疑问
    #1、带list可以先设置列表再赋值 2、绝对路径先存列表再赋值 3、参数必须要用赋值形式4、cc不是必传
    #cc的确是必传参数（抄送人）
    #yag.send(emaillist, 'zhangq0813@163.com', subjects,contentword,report)

    yag.send(to=emaillist, cc=emailcclist, subject=subjects, contents=contentword, attachments=report)

    print("the test email has send out !")



if __name__ == '__main__':

    # 默认按照ASCII码顺序执行
    test_dir = './test_case'
    #test.dir = './'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    '''
    #创建测试套件，按序执行？？？
    suite = unittest.TestSuite()
    suite.addTest(TestBaidu("test_search3"))
    suite.addTest(TestBaiduPage("test_baiduPage_case"))
    '''
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    html_report = './test_report/'+now_time+'result.html'
    fp = open(html_report, 'wb')
    #fp = open('./test_report/result.html','wb')
    
    runner = HTMLTestRunner(stream=fp,title="测试报告",\
                            description="描述",verbosity=2)

    #runner = unittest.TextTestRunner()
    runner.run(suit,0,False)  #0和False在python3.8及之后变成默认必传
    fp.close()
    send_eamil(html_report)
