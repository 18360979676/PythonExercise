#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import time, re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import requests
from io import BytesIO

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.set_window_size(1022, 1030)
except WebDriverException as e:
    print(e)
element = driver.find_element_by_xpath(r'//div/div[@class="JDJRV-smallimg"]/img')
ActionChains(driver).click_and_hold(on_element=element).perform()

ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=185, yoffset=0).perform()
ActionChains(driver).release(on_element=element).perform()
