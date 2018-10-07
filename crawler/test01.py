#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import requests

'''
    python爬虫系列二：Python爬虫准备：认识urllib/urllib2与requests
'''

'''
    urllib/urllib2的get请求方式
'''
# values = {}
# values['username'] = '136xxxx0839'
# values['password'] = '123xxx'
# data = urllib.urlencode(values)  # 这里注意转换格式
# url = 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
# getUrl = url + '?' + data
# request = urllib2.Request(getUrl)
# response = urllib2.urlopen(request)
# print response.read()
# print getUrl

'''
    urllib/urllib2的post请求方式
'''
# values = {}
# values['username'] = '136xxxx0839'
# values['password'] = '123xxx'
# data = urllib.urlencode(values)
# url = 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()


'''
    requests的响应和编码
'''
# url = 'http://www.baidu.com'
# res = requests.get(url)
# print type(res)
# print res.status_code
# print res.encoding
# print res.cookies
# print res.content
# ---------结果------------------
# <class 'requests.models.Response'>
# 200
# ISO-8859-1
# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>


'''
    requests的get请求方式
'''
# values = {'user': 'aaa', 'id': '123'}
# url = 'http://www.baidu.com'
# r = requests.get(url, values)
# print r.url


'''
    requests的post请求方式
'''
# values = {'user': 'aaa', 'id': '123'}
# url = 'http://www.baidu.com'
# r = requests.post(url, values)
# print r.url


'''
    requests的header处理
'''
# url = 'https://www.baidu.com/'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
# }
# url = 'http://www.baidu.com/'
# r = requests.get(url, headers=header)
# print r.content


'''
    响应码code与响应头headers处理
'''

# url = 'https://www.baidu.com'
# r = requests.get(url)
#
# if r.status_code == requests.codes.ok:
#     print r.status_code
#     print r.headers
#     print r.headers.get('content-type')  # 推荐用这种get方式获取头部字段
# else:
#     r.raise_for_status()


'''
    cookies处理
'''
# url = 'https://www.baidu.com'
# res = requests.get(url)
# print res.cookies
# print res.cookies.keys()
# ------------结果---------------------
# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# ['BDORZ']


''''
    重定向与历史消息
'''
# url = 'http://www.baidu.com'
# res = requests.get(url, allow_redirects=True)
# print res.status_code  # 200
# print res.history  # []
# print res.url


'''
    代理设置
'''
# proxis = {
#     'http': 'http://www.baidu.com',
#     'http': 'http://www.qq.com',
#     'http': 'http://www.sohu.com',
#
# }
#
# url = 'http://www.baidu.com'
# r = requests.get(url, proxies=proxis)
# print r.url
