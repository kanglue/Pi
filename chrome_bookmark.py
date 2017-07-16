#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'chrome bookmark'

__author__ = 'jianglei'

import requests
import os
import sys
from lxml import etree

class BookMark:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        print('loading file')
        with open(self.file_name, 'r') as f:
            while True:
                block = f.read(1024)
                print(block)
                if block:
                    yield block
                else:
                    return

    def load(self):
        print('loading file')
        with open(self.file_name, 'r') as f:
            xml = f.read()
            #print(xml)
            print('==============================================================')
            html = etree.HTML(xml)

            result = html.xpath('//a')
            print(len(result))

            for href in result:
                url = href.attrib['href']

                try:
                    r = requests.get(url, timeout=5)
                    if r.status_code != 200:
                        print(url)
                except Exception as e:
                    print(e)
                finally:
                    pass

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=')

if __name__=='__main__':
    if len(sys.argv) != 1:
        print('Parameter error.')
    bookmark = BookMark('/Users/jianglei/Documents/bookmarks_7_15_17.html')
    bookmark.load()
    #bookmark.read()
