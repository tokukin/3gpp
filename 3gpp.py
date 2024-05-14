# -*- coding: utf-8 -*-
#读取网站信息
import requests
from bs4 import BeautifulSoup
#使用requests库获取网页信息
response = requests.get('https://www.3gpp.org/ftp/Specs/archive/')
soup = BeautifulSoup(response.text, 'html.parser')  
print(soup.prettify())
