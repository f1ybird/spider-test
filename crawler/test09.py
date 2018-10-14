# !/usr/bin/python
# -*- coding:UTF-8 -*-


import json
import os
import urllib
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Yuan(object):
    """
    用Python来找你喜欢的妹子(二)
    """

    def __init__(self, **kwargs):
        self.gender = kwargs['gender']
        self.startage = kwargs['startage']
        self.endgage = kwargs['endgage']
        self.startheight = kwargs['startheight']
        self.endheight = kwargs['endheight']
        self.marry = kwargs['marry']
        self.salary = kwargs['salary']
        self.education = kwargs['education']
        self.cityid = kwargs['cityid']

    def craw_data(self):
        """
        数据抓取
        :return:
        """
        headers = {
            'Referer': 'http://www.lovewzly.com/jiaoyou.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
        }
        page = 1
        while True:
            query_data = {
                'page': page,
                'gender': self.gender,
                'startage': self.startage,
                'endage': self.endgage,
                'stratheight': self.startheight,
                'endheight': self.endheight,
                'marry': self.marry,
                'salary': self.salary,
                'education': self.education,
                'cityid': self.cityid
            }
            url = 'http://www.lovewzly.com/api/user/pc/list/search?' + urllib.urlencode(query_data)
            print url
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req).read()
            # print response
            self.parse_data(response)
            page += 1

    def parse_data(self, response):
        """
        数据解析
        :param response:
        :return:
        """
        persons = json.loads(response).get('data').get('list')
        if persons is None:
            print '数据已经请求完毕'
            return

        for person in persons:
            nick = person.get('username')
            gender = person.get('gender')
            age = 2018 - int(person.get('birthdayyear'))
            address = person.get('city')
            heart = person.get('monolog')
            height = person.get('height')
            img_url = person.get('avatar')
            education = person.get('education')
            print nick, age, height, address, heart, education
            self.store_info(nick, age, height, address, heart, education, img_url)
            # self.store_info_execl(nick, age, height, address, heart, education, img_url)

    def store_info(self, nick, age, height, address, heart, education, img_url):
        """
        存照片,与他们的内心独白
        """
        if age < 22:
            tag = '22岁以下'
        elif 22 <= age < 28:
            tag = '22-28岁'
        elif 28 <= age < 32:
            tag = '28-32岁'
        elif 32 <= age:
            tag = '32岁以上'
        filename = u'{}岁_身高{}_学历{}_{}_{}.jpg'.format(age, height, education, address, nick)

        try:
            # 补全文件目录
            image_path = u'E:/store/pic/{}'.format(tag)
            # 判断文件夹是否存在。
            if not os.path.exists(image_path):
                os.makedirs(image_path)
                print image_path + ' 创建成功'

            # 注意这里是写入图片，要用二进制格式写入。
            with open(image_path + '/' + filename, 'wb') as f:
                f.write(urllib.urlopen(img_url).read())

            txt_path = u'E:/store/txt'
            txt_name = u'内心独白.txt'
            # 判断文件夹是否存在。
            if not os.path.exists(txt_path):
                os.makedirs(txt_path)
                print txt_path + ' 创建成功'

            # 写入txt文本
            with open(txt_path + '/' + txt_name, 'a') as f:
                f.write(heart)
        except Exception as e:
            e.message

    # def store_info_execl(self, nick, age, height, address, heart, education, img_url):
    #     """
    #     存储到excel
    #     """
    #     person = []
    #     person.append(self.count)  # 正好是数据条
    #     person.append(nick)
    #     person.append(u'女' if self.gender == 2 else u'男')
    #     person.append(age)
    #     person.append(height)
    #     person.append(address)
    #     person.append(education)
    #     person.append(heart)
    #     person.append(img_url)
    #
    #     for j in range(len(person)):
    #         self.sheetInfo.write(self.count, j, person[j])
    #
    #     self.f.save(u'我主良缘.xlsx')
    #     self.count += 1
    #     print '插入了{}条数据'.format(self.count)


if __name__ == '__main__':
    dic = {
        'gender': '2',
        'startage': '21',
        'endgage': '30',
        'startheight': '',
        'endheight': '',
        'marry': '1',
        'salary': '',
        'education': '40',
        'cityid': '52'
    }
    y = Yuan(**dic)
    y.craw_data()
