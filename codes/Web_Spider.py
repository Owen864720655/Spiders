# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from lxml import etree
import requests as r

response =  r.get('http://www.meizitu.com/a/')

response.enconding = 'gbk'
html = response.text;

selector = etree.HTML(html)
content = selector.xpath('//img')

i=0
for each in content:
    src = each.xpath("@src")
    
    if len(src) == 0:
        src = each.xpath("@data-original")
        
    pic = r.get(src[0])
    
    f = open("pic\\" + str(i) + ".jpg", "wb")
    
    f.write(pic.content)
    f.close();
    i += 1
    print i
print 'OK'

