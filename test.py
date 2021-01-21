'''
import os
import urllib.request, urllib.error, urllib.parse

url = input('Nhập url xuất phát:')
url_list = []

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('hello.html', 'wb')
f.write(webContent)
f.close
'''

import re, web_op, save

#Replace all white-space characters with the digit "9":

count = 1
a = input()
save.creat_dir(a)
url = input('Nhập url:')
b = save.file_name(url,count)
print(b)
content = web_op.read_content(url)
save.write_file(b,content)