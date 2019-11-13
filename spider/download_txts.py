# -*- coding:gbk -*-
__author__ = 'Administrator'
# 'Administrator' ΪԤ����ı�����Ϊ�㵱ǰ��¼�ļ�����û���

from bs4 import BeautifulSoup

import requests, sys

"""
��˵��:���ء���Ȥ������С˵��һ�����㡷
"""


class DownLoader(object):
    """
    ���캯��
    """
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []  # ����½���
        self.urls = []   # ����½�����
        self.nums = []   # �½���
    """
    ����˵������ȡ��������
    """
    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = 'gbk'  # ָ����ҳ��������
        html = req.text()
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
        dl.writer(dl.names[i], '../publicFile/һ������.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("������:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('��һ�����㡷�������')
