#-*- coding:utf-8 -*-
__author__ = 'An'
import urllib2
import pycurl
import string
import cStringIO
import time
from nvdspider import NVD
from cnnvdspider import CNNVD
class Main():

    def __init__(self):
        #self.starturl = "http://android.scap.org.cn/avd_list.php?type=android&level=ker&p="
        #self.starturl = "http://android.scap.org.cn/avd_list.php?type=android&native=true&p="
        #self.starturl = "http://android.scap.org.cn/avd_list.php?type=android&level=lib&p="
        #self.starturl = "http://android.scap.org.cn/avd_list.php?type=android&level=app&p="
        #self.starturl = "http://android.scap.org.cn/avd_list.php?type=android&level=app&native=true&p="
        #self.starturl = "http://android.scap.org.cn/avd_list.php?type=android&level=app&native=false&p="
        #self.starturl = "http://android.scap.org.cn/avd_list.php?type=android&level=com&p="
        self.starturl = "http://cve.scap.org.cn/cve_list.php?action=vendor&keyword=oracle&p="
        self.pagelist = []
        self.flag_list = []

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

    def getUrlList(self, pageinfo):
        '''获取当前网页中的中所有的漏洞详细因袭链接
        '''
        infourllist = []
        inf_list = pageinfo.split('''</a></span><span style="padding-left:20px">''')[0:-1]
        infourl = ''
        infourllist = []
        for tmp in inf_list:
            infourllist.append(tmp.split('<h2><span><a href=')[1].split('"')[1])
            #infourl = tmp.split('<h2><span><a href=')[1].split('"')[1]
        return infourllist

    def getHomePageInfo(self):
        '''
        获取漏洞的页数信息
        '''
        pageinfo = self.getPageInfo(self.starturl + '1')
        self.getUrlList(pageinfo)
        pagenum = string.atoi(pageinfo.split('第1页 /')[1].split('页')[0].strip().split('共')[1])
        infourllist = []
        for num in range(1, pagenum+1):
            pageinfo = self.getPageInfo(self.starturl + str(num))
            infourllist = infourllist + self.getUrlList(pageinfo)
        print len(infourllist)
        return infourllist



    def getAVDInfo(self, url):
        '''
        获取漏洞详细网页的的漏洞信息
        :return:返回漏洞来源信息的字典
        '''
        self.flag_list = []
        #info = urllib2.urlopen(url).read()
        info = self.getPageInfo(url)
        if "未找到符合条件的" in info:
            cvd_info_dict = {}
            return cvd_info_dict
        #获取漏洞信息来源途径
        info = info.split('<!-- Baidu Button BEGIN -->')[0]
        info_list = info.split('<div id="')
        cvd_info = info_list[2:]
        #获取漏洞来源信息名称例如：NVD、CNNVD
        cvd_flag = info_list[1].split('</a></li>')[:-1]
        for tmp in cvd_flag:
            #print tmp.strip().split('<li><a')[1].split('">')[1]
            self.flag_list.append(tmp.strip().split('<li><a')[1].split('">')[1].lower())

        cvd_info_dict = {}
        if 'packetstorm' in self.flag_list:
            self.flag_list.remove('packetstorm')

        for tmp in cvd_info:
            if tmp.strip().startswith('packetstorm'):
                num = cvd_info.index(tmp)
                cvd_info_dict['packetstorm'] = tmp + cvd_info[num + 1]
            for flag in self.flag_list:
                if tmp.strip().startswith(flag.lower()):
                    cvd_info_dict[flag.lower()] = tmp
                    break
        return cvd_info_dict

    def start(self):
        file_name = "android_scap_"
        data_time = time.strftime('%Y%m%d', time.localtime(time.time()))
        file_name = file_name + data_time + '.txt'
        result = open(file_name, 'w')
        #获取漏洞的页数url信息
        infourllist = self.getHomePageInfo()
        for url in infourllist:
            print url
            cvd_info_dict = self.getAVDInfo(url)
            url_name = url.split('http://cve.scap.org.cn/')[1].split('.html')[0]

            if cvd_info_dict.has_key('nvd'):
                obj = NVD()
                result.write('漏洞编号:' + url_name + '\n')
                info_basic_dict = obj.getPageInfo(cvd_info_dict['nvd'])
                for (key, value) in info_basic_dict.iteritems():
                    result.write(key+value+'\n')
            # if cvd_info_dict.has_key('cnnvd'):
            #     obj = CNNVD()
            #     result.write('漏洞编号:' + url_name + '\n')
            #     info_basic_dict = obj.getPageInfo(cvd_info_dict['cnnvd'])
            #     for (key, value) in info_basic_dict.iteritems():
            #         result.write(key+value+'\n')
            #     result.write('\n')
if __name__ == "__main__":
    obj = Main()
    obj.start()