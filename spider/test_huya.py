#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   18360979676@qq.com
@License :   (C)Copyright 2016-2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/12 14:09   yezhu      1.0         None
--------------------- 
"""
# noinspection PyProtectedMember
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
import requests, time, urllib3


class GetHuYa(object):
    def __init__(self, server=None):
        self.server = server

    def get_content(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        req = requests.get(url=self.server, verify=False)
        only_tags_with_class_tag_right = SoupStrainer('em', {'class': 'tag-blue'})
        html_doc = req.text
        # noinspection SpellCheckingInspection
        content = BeautifulSoup(html_doc, 'html.parser', parse_only=only_tags_with_class_tag_right)
        print(content.find('em').get('class'))

    # noinspection PyMethodMayBeStatic
    def debug_hu_ya_video(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # noinspection SpellCheckingInspection
        # driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        try:
            driver.maximize_window()
        except WebDriverException as e:
            print(e)
        driver.get(self.server)
        time.sleep(2)
        driver.find_element_by_link_text('一起看').click()
        wait = WebDriverWait(driver, 4, 1)  # 显示等待
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
        driver.find_element_by_class_name('J_hdLg').click()
        time.sleep(1)
        driver.switch_to.frame('UDBSdkLgn_iframe')
        driver.find_element_by_class_name('udb-input-account').send_keys('18360979676')
        driver.find_element_by_class_name('udb-input-pw').send_keys('lyl123456')
        driver.find_element_by_id('login-btn').click()
        wait.until(lambda x: x.find_element_by_xpath("//ul[@id=\"js-live-list\"]/li/a[contains(text(),\"山鸡哥\")]")).click()
        # 截屏
        driver.save_screenshot('../publicFile/img/test_huya/huya_detail.png')
        need_handle = driver.window_handles[len(driver.window_handles) - 1]
        for item_tab in driver.window_handles:
            if item_tab != need_handle:
                driver.switch_to.window(item_tab)
                driver.close()
        driver.switch_to.window(need_handle)
        time.sleep(2)
        driver.execute_script('$(arguments[0]).attr(\'value\',\'大爷的\');$(arguments[1]).addClass(\'enable\').click();', driver.find_element_by_id('pub_msg_input'), driver.find_element_by_id('msg_send_bt'))
        time.sleep(1000)
        print(driver.get_cookies())


if __name__ == "__main__":
    get_hu_ya = GetHuYa("https://www.huya.com/")
    get_hu_ya.debug_hu_ya_video()
    # get_hu_ya.get_content()
