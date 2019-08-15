#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   simplyDemo.py    
@Contact :   18360979676@qq.com
@License :   (C)Copyright 2016-2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/11 9:00   yezhu      1.0         None
--------------------- 
"""

import wx

app = wx.App()
window = wx.Frame(None, title="wxPython你好!", size=(700, 550))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 100))
window.Show(True)
app.MainLoop()
