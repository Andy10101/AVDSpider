#-*- coding:utf-8 -*-
__author__ = 'An'
class CNNVD():
    def __init__(self):
        self.flag_list = []
        self.inf_dict = {u'漏洞名称：':u'',
                         u'紧急程度：':u'',
                         u'发布日期：':u'',
                         u'漏洞类型：':u'',
                         u'更新日期：':u'',
                         u'攻击路径：':u'',
                         u'详细介绍：':u''}

    def getPageInfo(self, info):
        info = info.replace('&nbsp;', '')
        info_basic = info.split('</table>')[0].strip().split('<table')[1].strip()
        info_basic_list = info_basic.split('<tr>')[1:]
        #print info_basic_list
        info_dict = {}
        for tmp in info_basic_list:
            info_list = tmp.split('</td>')[:-1]
            for tmp in info_list:
                if '<label>' in tmp:
                    tmp_list = tmp.split('<label>')[1].split('</label>')
                    info_dict[tmp_list[0].strip()] = tmp_list[1].strip()
                elif tmp.strip() == '<td></td>':
                    pass
                else:
                    if info_dict.has_key('详细介绍:'):
                        info_dict['详细介绍:'] = tmp.split('">')[1].replace('<br/>', '')
        print info_dict
        return info_dict
