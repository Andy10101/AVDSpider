#-*- coding:utf-8 -*-
__author__ = 'Andy'
import urllib2

class SecurityFocus():
    def __init__(self, url):
        self.url = url
        self.flag_list = []
        self.inf_dict = {u'漏洞名称：':u'',
                         u'漏洞位置：':u'',
                         u'利用方式：':u'',
                         u'漏洞影响：':u'',
                         u'解决方式：':u'',
                         u'漏洞利用：':u'',
                         u'公开方式：':u'',
                         u'漏洞描述：':u'',
                         u'解决方案：':u''}

    def getPageInfo(self):
        info = urllib2.urlopen(self.url).read()
        info = info.split('<!-- Baidu Button BEGIN -->')[0]
        #print info
        info_list = info.split('<div id="')
        cvd_info = info_list[2:]
        #print cvd_info
        cvd_flag = info_list[1].split('</a></li>')[:-1]
        for tmp in cvd_flag:
            print tmp.strip().split('<li><a')[1].split('">')[1]
            self.flag_list.append(tmp.strip().split('<li><a')[1].split('">')[1].lower())
        cvd_info_dict = {}
        self.flag_list.remove('packetstorm')

        for tmp in cvd_info:
            if tmp.strip().startswith('packetstorm'):
                num = cvd_info.index(tmp)
                cvd_info_dict['packetstorm'] = tmp + cvd_info[num + 1]
            for flag in self.flag_list:
                if tmp.strip().startswith(flag.lower()):
                    cvd_info_dict[flag.lower()] = tmp
                    break

        print cvd_info_dict['nvd']
if __name__ == "__main__":
    obj = SecurityFocus("http://cve.scap.org.cn/OSVDB/100299.html")
    obj.getPageInfo()
