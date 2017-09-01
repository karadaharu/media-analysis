#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.nikkei.com/article/DGXLASDC01H26_R00C17A9000000/")
soup = BeautifulSoup(html)
a = soup.find("div", class_="cmn-article_text");
p = a.find_all("p")

article = ""
for r in p:
    article = article + r.text

print(article)