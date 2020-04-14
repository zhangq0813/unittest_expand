from test_classpkg.objSelfLocate.basePageObject import BasePage
from poium import PageElement

class BaiduPage(BasePage):

    url = "https://www.baidu.com"

    '''方法一：自定义方法元素定位
    def search_input(self,search_key):
        self.by_id("kw").send_keys(search_key)
        
    def search_button(self):
        self.by_id("su").click()
    '''
    '''方法二：poium方法元素定位'''
    search_input = PageElement(id_='kw')
    search_button = PageElement(id_='su')
