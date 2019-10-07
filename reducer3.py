#!/usr/bin/env python
# coding: utf-8

# In[1]:


from operator import itemgetter
from collections import defaultdict
import sys
ti={}
ti = defaultdict(list)
dict_ip_count = {}
timee=[]
countt=[]
for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num
    except ValueError:
        pass
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1),reverse=True)
for ip, count in sorted_dict_ip_count:
    time,i =ip.split('_')
    if count not in countt:
        countt.append(count)
        ti[time].append(i)
    elif count in countt:
        ti[time].append(i)
        if len(ti[time])>=3 and time not in timee:
            timee.append(time)
            print ('%s\t%s' % (time, ti[time]))
        else:
            continue
    


# In[ ]:




