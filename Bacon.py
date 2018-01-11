# -*- coding: utf-8 -*-

# @Time     : 2018/1/11 10:59
# @Author   : Lavender
# @File     : Bacon.py
# @Software : PyCharm Community Edition

d = {'a':'aaaaa','b':'aaaab','c':'aaaba','d':'aaabb','e':'aabaa','f':'aabab','g':'aabba','h':'aabbb','i':'abaaa','j':'abaab',
     'k':'ababa','l':'ababb','m':'abbaa','n':'abbab','o':'abbba','p':'abbbb','q':'baaaa','r':'baaab','s':'baaba','t':'baabb',
     'u':'babaa','v':'babab','w':'babba','x':'babbb','y':'bbaaa','z':'bbaab'}
s = 'DCCDCCCDDDCDCCCDDCCCCCCCCCDDCDCCCCDCCCCC CDCCCDCCDC CCCDCCDDDCCDDDCCDCDD'
s = s.replace('C','a').replace('D','b')
print(s)
# s = s.replace('C','b').replace('D','a')
# print(s)
result = ''
i = 0
while i < len(s):
    if s[i].isalpha():
        if s[i:i+5] in d.values():
            r = [k for k,v in d.items() if v == s[i:i+5]]
            result += r[0]
        i += 5
    else:
        i += 1

print(result.upper())