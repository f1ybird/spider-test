#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lxml import etree
import requests

'''
    python爬虫系列三：Python爬虫：现学现用xpath爬取豆瓣音乐分步测试代码
    测试网址：https://music.douban.com/top250
'''

# s=etree.HTML(源码) #将源码转化为能被XPath匹配的格式
# s.xpath(xpath表达式) #返回为一列表

# -------xpath基础语法----------------------

# // 双斜杠 定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表的形式返回。
#
# / 单斜杠 寻找当前标签路径的下一层路径标签或者对当前路标签内容进行操作
#
# /text() 获取当前路径下的文本内容
#
# /@xxxx 提取当前路径下标签的属性值
#
# | 可选符 使用|可选取若干个路径 如//p | //div 即在当前路径下选取所有符合条件的p标签和div标签。
#
# . 点 用来选取当前节点
#
# .. 双点 选取当前节点的父节点

'''
    爬取豆瓣音乐前250条：https://music.douban.com/top250
'''
url = 'https://music.douban.com/top250'
html = requests.get(url).text
# print html
s = etree.HTML(html)

# 获取单条数据

# 获取歌曲名字
title = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a[1]/text()')[0]
print title.strip()
# 评分
score = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[2]/text()')[0]
print score.strip()
# 评价人数
numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[3]/text()')[0]
print numbers.strip().replace('(', '').replace(')', '').strip()
href = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a[1]/@href')[0]
print href.strip()
img = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[1]/a/img/@src')[0]
print img.strip()
# 结果
# We Sing. We Dance. We Steal Things.
# 9.1
# 101637人评价
# https://music.douban.com/subject/2995812/
# https://img3.doubanio.com/view/subject/s/public/s2967252.jpg


# 获取单个页面的多条数据，通过对比可知多条数据只是table的序号不一，所以去掉序号即可得到多条数据

# hrefs = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/@href')
# titles = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()')
# scores = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[2]/text()')
# numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[3]/text()')
# imgs = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[1]/a/img/@src')
# for i in range(25):
#     print hrefs[i], titles[i], scores[i], numbers[i], imgs[i]


# 提取公共的xpath前缀
# trs = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr')  # 先提取tr之前的节点集合
# for tr in trs:  # 遍历tr
#     href = tr.xpath('./td[2]/div/a/@href')[0]  # 注意新节点是tr下的节点
#     title = tr.xpath('./td[2]/div/a/text()')[0]
#     score = tr.xpath('./td[2]/div/div/span[2]/text()')[0]
#     number = tr.xpath('./td[2]/div/div/span[3]/text()')[0]
#     img = tr.xpath('./td[1]/a/img/@src')[0]
#     print href, title, score, number, img

# 获取多个页面的url
for i in range(10):
    url = 'https://music.douban.com/top250?start={}'.format(i * 25)
    print url
