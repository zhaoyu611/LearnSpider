#-*- coding: utf-8 -*-
# author: zhaoyu
# date: 2017.03.08
# 本脚本是http://www.itokoo.com/read.php?tid=31396的爬虫代码，用于将爱图客上ISHOW
# 子栏的所有图片名、下载链接、预览图等信息采集到本地

import os
import requests
from bs4 import BeautifulSoup

class itokoo(object):
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        self.root_url = "http://www.itokoo.com/read.php?tid=31396"

    def get_pic_name_and_link(self):
        """ 得到主页面上，所有套图的文件名和链接
            arugment:
                None
            return: 
                pic_name_list: [list] 套图名列表，每个元素是str
                pic_link_list: [list] 套图链接列表，每个元素是str
        """
        #巨坑!!! content能自动识别网站编码，优于text
        html = requests.get(self.root_url).content

        soup = BeautifulSoup(html,'lxml')
        pic_info_list=soup.find('div',class_="f14 mb10").find_all('a')
        pic_name_list=[] #构造列表存储图片名
        # pic_link_list=[] #构造列表存储图片链接
        for pic_info in pic_info_list:
            pic_link_list.append(pic_info['href'])
            # pic_name_list.append(pic_info.string)

        assert len(pic_name_list)==len(pic_link_list), "Please ensure the name and link have same numbers"
        for index in range(len(pic_link_list)):
            with open('test.txt','a') as f:
                # #NavigableString为unicode类型，不能直接写入文档，需要编码
                # f.write(pic_name_list[index].encode('gbk'))
                # f.write('\n')
                f.write(pic_link_list[index])
                f.write('\n')


if __name__ == '__main__':
    # step1: 得到主页面上，所有套图的文件名和链接
    # step2: 进入每个套图链接，得到文字说明、预览图、下载链接
    # step3: 保存资料到本地磁盘
    itokoo=itokoo()
    itokoo.get_pic_name_and_link()