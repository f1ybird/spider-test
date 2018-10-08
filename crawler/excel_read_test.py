#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd

'''
    python读excel测试代码
'''

data = xlrd.open_workbook('execl_file.xlsx')
table = data.sheets()[0]  # 通过索引顺序获取table, 一个execl文件一般都至少有一个table
print table.nrows  # 行数
print table.ncols  # 列数

for k in range(table.nrows):  # 遍历行数据
    print table.row_values(k)

for i in range(table.ncols):  # 便利列数据
    print table.col_values(i)

print table.cell(2, 2).value  # 获取单元格数据，前一个是行数，从0开始，后一个是列数，且列数从0开始

for a in range(1, table.nrows):  # 行数据，我正好要去掉第1行标题
    for b in range(table.ncols):
        print table.cell(a, b).value
    print '----------------------'
