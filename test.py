#-*- coding:utf-8 -*-
__author__ = 'An'
import urllib2

class MyUrl():
    def __init__(self):
        self.url = "http://cve.scap.org.cn/BID/45650.html"


    def start(self):
        info = urllib2.urlopen(self.url)
        infos = info.read()
        print infos

if __name__ == "__main__":
    obj = MyUrl()
    obj.start()


