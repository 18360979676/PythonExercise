#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import cv2
import time, random
import numpy as np
from selenium import webdriver
from urllib import request
from selenium.webdriver.common.action_chains import ActionChains
brower = webdriver.Chrome()


def loadpage(userid, password):
    url = 'https://passport.jd.com/new/login.aspx?'
    brower.get(url)
    brower.set_window_size(1022, 1030)
    time.sleep(3)
    s1 = r'//div/div[@class="login-tab login-tab-r"]/a'
    userlogin = brower.find_element_by_xpath(s1)
    userlogin.click()
    username = brower.find_element_by_id('loginname')
    username.send_keys(userid)
    userpswd = brower.find_element_by_id('nloginpwd')
    userpswd.send_keys(password)
    brower.find_element_by_id('loginsubmit').click()
    time.sleep(3)
    getpic()


def getpic():
    s2 = r'//div/div[@class="JDJRV-bigimg"]/img'
    s3 = r'//div/div[@class="JDJRV-smallimg"]/img'
    bigimg = brower.find_element_by_xpath(s2).get_attribute('src')
    smallimg = brower.find_element_by_xpath(s3).get_attribute('src')
    backimg = './img/backimg.png'
    slideimg = './img/slideimg.png'
    request.urlretrieve(bigimg, backimg)
    request.urlretrieve(smallimg, slideimg)
    # 获取图片并灰度化
    block = cv2.imread(slideimg, 0)
    template = cv2.imread(backimg, 0)
    # 二值化后的图片名称
    blockname = './img/block.jpg'
    templatename = './img/template.jpg'

    # # 将二值化后的图片进行保存
    cv2.imwrite(blockname, block)
    cv2.imwrite(templatename, template)
    block = cv2.imread(blockname)
    block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
    block = abs(255 - block)
    cv2.imwrite(blockname, block)
    block = cv2.imread(blockname)
    template = cv2.imread(templatename)

    # 获取偏移量
    result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)  # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
    x, y = np.unravel_index(result.argmax(), result.shape)

    # 获取滑块
    element = brower.find_element_by_xpath(s3)
    ActionChains(brower).click_and_hold(on_element=element).perform()

    ActionChains(brower).move_to_element_with_offset(to_element=element, xoffset=y, yoffset=0).perform()
    ActionChains(brower).release(on_element=element).perform()


if __name__ == '__main__':
    loginname = '骑猪也浪漫'
    nloginpwd = 'zxcvbnm123'
    loadpage(loginname, nloginpwd)
