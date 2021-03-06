#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import requests
from bs4 import BeautifulSoup
import re

html = requests.get('http://baike.baidu.com/view/284853.htm').content  # .content保存byte信息。.text则是编码好的信息。
bs_obj = BeautifulSoup(html,"html.parser")

#findAll(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)
#recursive=False表示只搜索直接儿子，否则搜索整个子树，默认为True。
#findAll(“a”）
#findAll(“a”, href=“”)
#findAll(“div”, class=“”)
#findAll(“button”, id=“”)

#a_list = bs_obj.findAll("a")
a_list = bs_obj.findAll("a",href=re.compile("\.baidu\.com\w?"))
print (a_list)

for aa in a_list:
    if not aa.find("img"):
        if aa.attrs.get('href'):
            print (aa.text, aa.attrs['href'])
        