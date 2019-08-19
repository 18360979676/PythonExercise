# -*- coding: utf-8 -*-
import urllib.request
import re


# 获取网页的html
def gethtml(url):
	response = urllib.request.Request(url, headers=header)
	page = urllib.request.urlopen(response)
	html = page.read().decode('utf-8')
	print(html)
	return html


# 获取图片对应的src属性
def getimg(html):
	src = r'http://[^\s]*?\.jpg'
	imgre = re.compile(src)
	imglist = re.findall(imgre, html)
	x = 0
	for imgurl in imglist:
		urllib.request.urlretrieve(imgurl, '../publicFile/img/test_urllib/%s.jpg' % x)
		x += 1
		print(imgurl)


if __name__ == '__main__':

	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
	html_text = gethtml("http://tieba.baidu.com/p/6229338729")
	getimg(html_text)
	print("ok")
