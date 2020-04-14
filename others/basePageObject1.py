import time

class BasePage:
    """基础page层，封装一些常用方法"""
    #初始化驱动
    def __init__(self,driver):
        self.driver = driver

    #打开页面方法
    def open(self,url = None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    #id定位
    def by_id(self,id):
        return self.driver.find_element_by_id(id)

    #name定位
    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    # name定位
    def by_class(self, calss_name):
        return self.driver.find_element_by_class(calss_name)

    #tag标签定位
    def by_tag(self,tag_name):
        return self.driver.find_element_by_tag(tag_name)

    #link_text定位
    def by_link_text(self,link_text):
        return self.driver.find_element_by_link_text(link_text)

    #partical_link_text定位
    def by_partical_link_text(self, partical_link_text):
        return self.driver.find_element_by_partical_link_text(partical_link_text)

    #xpath定位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    #css定位
    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    #获取网页标题
    def get_title(self):
        return self.driver.title

    #获取页面text，仅使用xpath定位
    def get_text(self,xpath):
        return self.by_xpath(xpath).text

    #执行JS脚本
    def js(self,script):
        self.driver.execute_script(script)