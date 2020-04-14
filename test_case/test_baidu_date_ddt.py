import unittest
from time import sleep
from selenium import webdriver
#from parameterized import parameterized
from ddt import ddt,data,file_data,unpack


@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = ("https://www.baidu.com")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(1)
    '''#注释缩进要保持同内容一致
    @parameterized.expand([
        ("case1","selenium"),
        ("case2","unittest"),
        ("case3","pytest")
    ])
    def test_baidu_search_selenium(self,name,search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    '''
    '''
    #参数化 装饰器tuple
    
    @data(("case1","selenium"),("case2","ddt"),("case3","unittest"))
    #@data(("case1", "selenium"))
    @unpack
    def test_search1(self, case, search_key):
        print("第一组测试用例：", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    
    #参数化 装饰器list
    @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "unittest"])
    @unpack
    def test_search2(self, case, search_key):
        print("第二组测试用例：",case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")
    '''

    # 参数化 装饰器dictionaris
    @data({"search_key":"selenium"}, {"search_key": "ddt"},{"search_key":"unittest"})
    @unpack
    def test_search3(self,search_key):
        print("第三组测试用例：", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_1百度搜索")

if __name__ == '__main__':
    unittest.main(verbosity=2)
