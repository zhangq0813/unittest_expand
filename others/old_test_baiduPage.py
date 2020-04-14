import unittest
from basePageBaidu import BaiduPage
from time import sleep
from selenium import webdriver
from ddt import ddt,data,unpack

#课题1，数据参数化----》通过
#课题2，运行控制器控制案例顺序，案例获取从多个目录
#课题3，用例报错了需要继续执行-------》断言失败了，是正常执行得
#问题4，为何断言不匹配，案例失败了，但是生成得测试报告是通过得---》执行文件和当前文件不匹配导致
@ddt
class TestBaiduPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data({"search_key":"selenium"}, {"search_key": "ddt"},{"search_key":"unittest"})
    @unpack
    def test_baiduPage_case(self,search_key):
        page = BaiduPage(self.driver)
        #page.open("https://www.baidu.com")
        page.open()
        '''方法一：自定义方法元素定位
        page.search_input(search_key)
        page.search_button()
        '''
        '''方法二：poium方法元素定位'''
        page.search_input = search_key
        page.search_button.click()

        sleep(2)
        self.assertEqual(page.get_title(),search_key+"_百度搜索")
        print(page.get_title())


if __name__ == "__main__":
    unittest.main(verbosity=2)

