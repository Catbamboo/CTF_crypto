# -*- coding: utf-8 -*-

# @Time     : 2018/1/11 10:35
# @Author   : Lavender
# @File     : QWE.py
# @Software : PyCharm Community Edition

# QWE
# The Q-W on the keyboard corresponds to the letter A-Z

a = 'abcdefghijklmnopqrstuvwxyz'
b = 'qwertyuiopasdfghjklzxcvbnm'
s = 'KIQLWTFCQGNSOO'
aa = ''
bb = ''
a = a.upper()
b = b.upper()
for i in s:
    n = a.index(i)
    bb += b[n]

for i in s:
    n = b.index(i)
    aa += a[n]

aa = reversed(aa)
for i in aa:
    print(i,end='')