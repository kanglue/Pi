#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

html = urlopen("http://www.iciba.com/initiative/")
bsObj=BeautifulSoup(html,"lxml")    #将html对象转化为BeautifulSoup对象

#音标
divList=bsObj.findAll("i",{"class":"new-speak-step"})
print("div list: " + str(len(divList)))
for span in divList:
    print(span.find_previous_sibling().text)

#词性
propList=bsObj.findAll("span",{"class":"prop"})
for prop in propList:
    print(prop.text)

#中文意
clearfixList=bsObj.findAll("li",{"class":"clearfix"})
print("中意： " + str(len(clearfixList)))
for clearfix in clearfixList:
    if not clearfix.p.text.strip() == '':
        print(">"+clearfix.p.text)

#柯林斯
spanList=bsObj.findAll("span",{"class":"family-chinese"})
print("柯林斯中意： " + str(len(spanList)))
for span in spanList:
    if not span.text.strip() == '':
        print(">>"+span.text)

spanEnList=bsObj.findAll("span",{"class":"family-english size-english prep-en"})
print("柯林斯英意： " + str(len(spanEnList)))
for spanEn in spanEnList:
    if not spanEn.text.strip() == '':
        print(">>>"+spanEn.text)

pEnList=bsObj.findAll("p",{"class":"family-english"})
print("例句： " + str(len(pEnList)))
for pEn in pEnList:
    if not pEn.text.strip() == '':
        print(">>>>"+pEn.text)