#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from operator import itemgetter
from collections import defaultdict
from operator import itemgetter
import re
import sys
d={}
d = defaultdict(list)
top={}
top = defaultdict(list)
timee=[]
dict_ip_count = {}
for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num
    except ValueError:
        pass
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
for i in sorted_dict_ip_count:
    ip = i[0]
    num=i[1]
    try:
        num = int(num)
        d[num].append(ip) 
    except ValueError:
        pass
sorted_dd = sorted(d.keys(),reverse=True)
for k in sorted_dd:
    try:
        for i in d[k]:
            time=re.findall('([[0-9]+:[0-9]+])',i)
            time=time[0]
            value=re.findall(']([0-9]\S+)',i)
            value=re.findall('([0-9]\S+)]',str(value))
            value=value[0]
            top[time].append(value)
        for time in top.keys():
            if len(top[time])>=3 and time not in timee:
                timee.append(time)
                for i in top[time]:
                    print('%s\t%s' %(time,i))
            else:
                continue
     except ValueError:
       pass
