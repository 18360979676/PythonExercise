#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import string, random, time


class Outlook(object):
    def __init__(self, loginaddress=None):
        """

        :param loginaddress: 登录页面
        """
        self.username = ""
        self.password = ""
        self.firsChar = string.ascii_letters + '_'
        self.otherChar = self.firsChar + string.digits
        self.driver = webdriver.Chrome()
        self.loginaddress = loginaddress

    def getname(self):
        """

        :return:自动生成指定长度的用户名称
        """
        while True:
            self.username = random.choice(self.firsChar)
            name_len = int(input("用户名长度"))
            for x in range(name_len - 1):
                self.username += random.choice(self.otherChar)
            print("{0}用户名是否符合你的要求：".format(self.username))
            choice = input('Y/N')
            if choice.lower() != 'n':
                break

    def getpwd(self):
        """

        :return:自动生成指定长度的用户密码
        """
        while True:
            self.password = ""
            pwd_len = int(input("密码长度:"))
            for x in range(pwd_len):
                self.password += random.choice(self.otherChar)
            print("{0}密码是否符合你的要求：".format(self.password))
            choice = input('Y/N')
            if choice.lower() != 'n':
                break

    def getyear(self):
        """

        :return: 生成年
        """
        return str(random.choice(range(1979, 1998)))

    def getmonth(self):
        """

        :return:生成月份
        """
        return str(random.choice(range(1, 13)))

    def getday(self):
        """

        :return:生成天/日期
        """
        return str(random.choice(range(1, 29)))

    def run(self):
        """
        生成用户名和密码，启动页面
        :return:
        """
        self.getname()
        self.getpwd()
        self.driver.get(self.loginaddress)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        try:
            # 定位页面元素
            self.driver.find_element_by_id('MemberName').send_keys(self.username)
            self.driver.find_element_by_id('iSignupAction').click()
            self.driver.find_element_by_id('PasswordInput').send_keys(self.password)
            time.sleep(1.8)
            self.driver.find_element_by_id('ShowHidePasswordCheckbox').click()
            self.driver.find_element_by_id('iOptinEmail').click()
            self.driver.find_element_by_id('iSignupAction').click()
            self.driver.find_element_by_id('LastName').send_keys(input('请输入姓:').capitalize())
            self.driver.find_element_by_id('FirstName').send_keys(input('请输入名:').capitalize())
            self.driver.find_element_by_id('iSignupAction').click()
            Select(self.driver.find_element(By.ID, 'BirthYear')).select_by_value(self.getyear())
            Select(self.driver.find_element(By.ID, 'BirthMonth')).select_by_value(self.getmonth())
            Select(self.driver.find_element(By.ID, 'BirthDay')).select_by_value(self.getday())
            time.sleep(6)
            self.driver.find_element(By.ID, "iSignupAction").click()

        except NoSuchElementException as e:
            pass

    def findword(self):
        pass


if __name__ == '__main__':
    loginAction = Outlook("https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1573615080&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d02bad4c6-e96c-375a-14cc-6aa339223feb&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=38b4786732ba413fa8fd495a0f40b1a7")
    loginAction.run()
