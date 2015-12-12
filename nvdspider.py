#-*- coding:utf-8 -*-
__author__ = 'An'
import urllib2

class NVD():
    def __init__(self):
        self.flag_list = []
        self.inf_dict = {u'CVSS分值：':u'',
                         u'机密性影响：':u'',
                         u'完整性影响：':u'',
                         u'可用性影响：':u'',
                         u'攻击复杂度：':u'',
                         u'攻击向量：':u'',
                         u'身份认证：':u'',
                         u'受影响的平台与产品：':u''}

    def getPageInfo(self, info):
        info_basic = info.split('CPE (受影响的平台与产品)')[0].strip().split('</table>')[0]
        info_basic_list = info_basic.split('<tr>')[1:]
        #print info_basic_list
        info_dict = {}
        for tmp in info_basic_list:
            info_list = tmp.split('</td>')[:-1]
            info_dict[info_list[0].split('>')[1]] = info_list[2].split('>')[1]

        return info_dict

if __name__ == "__main__":
    obj = NVD()
    obj.getPageInfo()
