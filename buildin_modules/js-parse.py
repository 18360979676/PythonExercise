#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

import sys
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    # 归正格式问题
    def handle_starttag(self, tag, attrs):
        sys.stdout.write('<%s' % tag)
        for attr in attrs:
            sys.stdout.write(' ' + attr[0] + '"=' + attr[1] + '"')
        print('>')

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s' % tag)
        for attr in attrs:
            sys.stdout.write(' ' + attr[0] + '=' + attr[1])
        sys.stdout.write('/>')

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html><head></head><body>
<!-- test html parser -->
    <p data-first=\"1\" data-second=\"2\">Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
