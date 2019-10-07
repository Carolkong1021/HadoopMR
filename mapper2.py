#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import sys
from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
d={}
d = defaultdict(list)
for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        d[num].append(ip) 
    except ValueError:
        pass
od = OrderedDict(reversed(sorted(d.items())))
for num,ip in od.items():
     for i in ip:
         print ('%s\t%s\n' % (num, i))

