# !/usr/bin/python
# -*- coding:UTF-8 -*-


import requests
from lxml import etree

'''
    Python爬取大量数据时，如何防止IP被封

    1.添加请求头
    2.添加代理ip

    以下是添加代理ip后的完整代码
'''


def getUrl():
    for i in range(70):
        url = 'http://task.zbj.com/t-ppsj/page{}.html'.format(i + 1)
        spiderPage(url)


def spiderPage(url):
    if url is None:
        return None

    try:
        proxies = {
            # 'https': 'https://106.75.164.15:3128',
            'http': 'http://118.190.95.35:9001'
        }
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'

        headers = {'User-Agent': user_agent}
        htmlText = requests.get(url, headers=headers, proxies=proxies).text

        selector = etree.HTML(htmlText)
        divs = selector.xpath('//*[@id="utopia_widget_7"]/div[1]/div')

        for div in divs:
            title = div.xpath('./a/p[1]/span[2]/text()')
            href = div.xpath('./a/@href')
            price = div.xpath('./a/p[2]/b/text()')
            subTitle = div.xpath('./a/p[3]/text()')
            deadline = div.xpath('./a/p[2]/span/text()')
            price = price[0] if len(price) > 0 else ''  # python的三目运算 :为真时的结果 if 判定条件 else 为假时的结果
            title = title[0] if len(title) > 0 else ''
            href = href[0] if len(href) > 0 else ''
            subTitle = subTitle[0] if len(subTitle) > 0 else ''
            deadline = deadline[0] if len(deadline) > 0 else ''
            print title, price, 'https:' + href, subTitle, deadline
            print '---------------------------------------------------------------------------------------'
            # spiderDetail(href)
    except Exception, e:
        print '出错', e.message


def spiderDetail(url):
    if url is None:
        return None

    try:
        htmlText = requests.get(url).text
        selector = etree.HTML(htmlText)
        aboutHref = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/div/p[1]/a/@href')
        price = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/div/p[1]/text()')
        title = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/h2/text()')
        contentDetail = selector.xpath('//*[@id="utopia_widget_10"]/div[2]/div/div[1]/div[1]/text()')
        publishDate = selector.xpath('//*[@id="utopia_widget_10"]/div[2]/div/div[1]/p/text()')
        aboutHref = aboutHref[0] if len(aboutHref) > 0 else ''  # python的三目运算 :为真时的结果 if 判定条件 else 为假时的结果
        price = price[0] if len(price) > 0 else ''
        title = title[0] if len(title) > 0 else ''
        contentDetail = contentDetail[0] if len(contentDetail) > 0 else ''
        publishDate = publishDate[0] if len(publishDate) > 0 else ''
        print aboutHref, price, title, contentDetail, publishDate
    except:
        print '出错'


if '_main_':
    getUrl()
