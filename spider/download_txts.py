# -*- coding:gbk -*-
__author__ = 'Administrator'
# 'Administrator' ΪԤ����ı�����Ϊ�㵱ǰ��¼�ļ�����û���

from bs4 import BeautifulSoup

import requests, sys, string, random

"""
��˵��:���ء���Ȥ������С˵��һ�����㡷
"""


class DownLoader(object):
    """
    ���캯��
    """
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/42_42882/'
        self.names = []  # ����½���
        self.urls = []   # ����½�����
        self.nums = []   # �½���
    """
    ����˵������ȡ��������
    """
    def get_download_url(self):
        header_list = [
            # ����
            {"user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
            # ���
            {"user-agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
            # �ȸ�
            {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        ]
        req = requests.get(url=self.target, headers=random.choice(header_list))
        req.encoding = 'gbk'  # ָ����ҳ��������
        html = req.content
        div_bf = BeautifulSoup(html, "html5lib")
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), "html5lib")
        a = a_bf.find_all('a')
        self.nums = len(a[16:])
        for each in a[16:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
    ����˵������ȡ�½�����
    """
    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = 'gbk'  # ָ����ҳ��������
        html = req.text
        bf = BeautifulSoup(html, "html5lib")
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    """
    ����˵��:����ȡ����������д���ļ�
    """
    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = DownLoader()
    dl.get_download_url()
    print('��һ�����㡷��ʼ���أ�')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '../publicFile/Ҷ������ѩ.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("������:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('��Ҷ������ѩ���������')
