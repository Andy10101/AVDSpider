#-*- coding:utf-8 -*-
__author__ = 'An'
import codecs
class ReadFile():

    def __init__(self, path):
        self.path = path
        self.infos_list = []
        self.info_dict = {}

    def getInfo(self):
        info = codecs.open(self.path, 'r').readlines()

        for tmp in info:
            if tmp.startswith('OSVDBID:'):
                tmp_list = tmp.split(':')
                self.info_dict['OSVDBID:'] = tmp_list[1].strip()
            if tmp.startswith('CVE ID:'):
                tmp_list = tmp.split(':')
                self.info_dict['CVE ID:'] = tmp_list[1]+tmp_list[2].strip()
            if '漏洞信息' in tmp:
                tmp_list = tmp.split('	')
                self.info_dict['漏洞信息:'] = tmp_list[0].strip()
            if tmp.startswith('漏洞名称:'):
                tmp_list = tmp.split(':')
                self.info_dict['漏洞名称:'] = tmp_list[1].strip()
            if tmp.startswith('漏洞位置:'):
                tmp_list = tmp.split(':')
                self.info_dict['漏洞位置:'] = tmp_list[1].strip()
            if tmp.startswith('利用方式:'):
                tmp_list = tmp.split(':')
                self.info_dict['利用方式:'] = tmp_list[1].strip()
            if tmp.startswith('漏洞名称:'):
                tmp_list = tmp.split(':')
                self.info_dict['漏洞名称:'] = tmp_list[1].strip()
            if tmp.startswith('漏洞影响:'):
                tmp_list = tmp.split(':')
                self.info_dict['漏洞影响:'] = tmp_list[1].strip()
            if tmp.startswith('解决方式:'):
                tmp_list = tmp.split(':')
                self.info_dict['解决方式:'] = tmp_list[1].strip()
            if tmp.startswith('漏洞利用:'):
                tmp_list = tmp.split(':')
                self.info_dict['漏洞利用:'] = tmp_list[1].strip()
            if tmp.startswith('公开方式:'):
                tmp_list = tmp.split(':')
                self.info_dict['公开方式:'] = tmp_list[1].strip()
            if tmp.startswith('解决方案:'):
                tmp_list = tmp.split(':')
                self.info_dict['解决方案:'] = tmp_list[1].strip()
            if tmp.startswith('漏洞描述:'):
                tmp_list = tmp.split(':')
                self.info_dict['漏洞描述:'] = tmp_list[1].strip()
                self.infos_list.append(self.info_dict)
                self.info_dict = {}


    def start(self):
        self.getInfo()
        result = open(r'c:\Users\An\Desktop\cvdinfo_result.txt', 'w')
        print len(self.infos_list)
        for info_dict in self.infos_list:
            for key, values in info_dict.items():
                result.write(key+values + '\n')
            result.write('\n')

        result.close()

if __name__ == "__main__":
    obj = ReadFile(r'c:\Users\An\Desktop\cvdinfo.txt')
    obj.start()