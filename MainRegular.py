#-*- coding:utf-8 -*-
__author__ = 'An'
import pycurl
import re
import cStringIO


class Main():

    def __init__(self):
        self.starturl = "http://cve.scap.org.cn/OSVDB/100299.html"

    def getPageInfo(self, url):
        '''读取网页内容
        '''
        curl = pycurl.Curl()
        curl.setopt(pycurl.CONNECTTIMEOUT, 60)
        curl.setopt(pycurl.TIMEOUT, 300)
        curl.setopt(pycurl.URL, url)
        info = cStringIO.StringIO()
        curl.setopt(curl.WRITEFUNCTION, info.write)
        curl.perform()

        return info.getvalue()


    def getAVDInfo(self):
        '''
        获取漏洞详细网页的的漏洞信息
        :return:返回漏洞来源信息的字典
        '''
        url = 'http://cve.scap.org.cn/OSVDB/100299.html'
        cvd_info_dict = {}
        pageinfo = self.getPageInfo(url)
        #rule_nvd = '^<div id="nvd">([\s\S]*)<div id="cnnvd">'
        rule_nvd = r'<div id="nvd">([\s\S]*)<div id="cnnvd">'
        pattern = re.compile(rule_nvd)
        match = pattern.findall(pageinfo)

        # rule_nvd = r'%s(.+?)%s'%('<div id="nvd">', '</div>')
        # pattern = re.compile(rule_nvd, re.IGNORECASE)
        # match = pattern.match(pageinfo)

        # rule_nvd = r'<div id="nvd">(\d*)</div>(\d*)'
        # pattern = re.compile(r'<div id="nvd">\/(\d*)</div>')
        # match = pattern.search(pageinfo)
        if len(match):
            print match

        return cvd_info_dict

    def start(self):
        #获取漏洞的页数url信息
        infourllist = self.getAVDInfo()
if __name__ == "__main__":
    obj = Main()
    obj.start()