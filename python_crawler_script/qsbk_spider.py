# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time
from bs4 import BeautifulSoup
 
#糗事百科爬虫类
class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        self.joke_list = []
        self.enable = True
    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
 
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败,错误原因",e.reason
                return None
 
 
    #传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        soup = BeautifulSoup(pageCode)
        content =  soup.select('.content')
        result = []
        for con in content:
        	 result.append(str(content.index(con)) + con.span.text)
        return result
 
    def getOneStory(self):
        #遍历一页的段子
        self.joke_list = self.getPageItems(self.pageIndex)
        for joke in self.joke_list:
            print joke
            self.joke_list.pop(0)
            input = raw_input()
            if input == "Q":
                self.enable = False
                return	
    #开始方法
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        while self.enable:
            if len(self.joke_list) == 0:
                self.getOneStory()
 
 
spider = QSBK()
spider.start()
