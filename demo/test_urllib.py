# -*- coding: utf-8 -*-
import  urllib.request
import re

# 获取网页的html
def getHtml(url):
	response = urllib.request.Request(url, headers = header)
	page = urllib.request.urlopen(response)
	html = page.read().decode('utf-8')
	print(html)
	return html

# 获取图片对应的src属性
def getImg(html):
	src = r'http://[^\s]*?\.jpg'
	imgre = re.compile(src)
	imglist = re.findall(imgre, html)
	x = 0
	for imgurl in imglist:
		urllib.request.urlretrieve(imgurl, 'C:\Python34\demo\%s.jpg' % x)
		x += 1
		print(imgurl)

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
html = getHtml("http://tieba.baidu.com/p/6229338729")
getImg(html)
print("ok")