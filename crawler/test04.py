# !/usr/bin/python
# -*- coding: UTF-8 -*-

import requests  # http请求
import xlwt  # 写入excel
import xlrd  # 读取excel
from lxml import etree  # xpath
import os

'''
     把爬取的猪八戒数据插入到execl中
'''


class ZbjData(object):

    def __init__(self):
        self.f = xlwt.Workbook()  # 创建工作薄
        self.sheet1 = self.f.add_sheet(u'任务列表', cell_overwrite_ok=True)
        self.rowsTitle = [u'编号', u'标题', u'简介', u'价格', u'截止时间', u'链接']
        for i in range(0, len(self.rowsTitle)):
            self.sheet1.write(0, i, self.rowsTitle[i], self.set_style('Times new Roman', 220, True))

        filename = 'zbj.xls'  # 检测当前目录下是否有info.xls文件，如果有则清除以前保存文件
        if os.path.exists(filename):
            os.remove(filename)

        self.f.save(filename)

    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style

    def getUrl(self):
        for i in range(33):
            url = 'http://task.zbj.com/t-ppsj/page{}.html'.format(i + 1)
            self.spiderPage(url)

    def spiderPage(self, url):
        if url is None:
            return None

        try:
            data = xlrd.open_workbook('zbj.xls')
            table = data.sheets()[0]  # 通过索引顺序获取table, 一个execl文件一般都至少有一个table
            rowCount = table.nrows  # 获取行数   ，下次从这一行开始
            proxies = {
                'http': 'http://118.190.95.35:9001',
            }
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'

            headers = {'User-Agent': user_agent}
            htmlText = requests.get(url, headers=headers, proxies=proxies).text

            selector = etree.HTML(htmlText)
            divs = selector.xpath('//*[@id="utopia_widget_7"]/div[1]/div')
            m = 0
            for div in divs:
                title = div.xpath('./a/p[1]/span[2]/text()')
                href = div.xpath('./a/@href')
                price = div.xpath('./a/p[2]/b/text()')
                subTitle = div.xpath('./a/p[3]/text()')
                deadline = div.xpath('./a/p[2]/span/text()')
                price = price[0] if len(price) > 0 else ''  # python的三目运算 :为真时的结果 if 判定条件 else 为假时的结果
                title = title[0] if len(title) > 0 else ''
                href = 'http:' + href[0] if len(href) > 0 else ''
                subTitle = subTitle[0] if len(subTitle) > 0 else ''
                deadline = deadline[0] if len(deadline) > 0 else ''
                # print title, price, 'https:' + href, subTitle, deadline
                # print '---------------------------------------------------------------------------------------'
                # spiderDetail(href)
                # 拼装成一个集合
                data = []
                data.append(rowCount + m)  # 加个序号
                data.append(title)
                data.append(subTitle)
                data.append(price)
                data.append(deadline)
                data.append(href)

                for i in range(len(data)):
                    self.sheet1.write(rowCount + m, i, data[i])  # 写入数据到execl中

                m += 1  # 记录行数增量
                print m

        except Exception, e:
            print '出错', e.message

        finally:
            self.f.save('zbj.xls')


if '_main_':
    zbj = ZbjData()
    zbj.getUrl()
