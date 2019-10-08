#!/usr/bin/env python
# coding: utf-8

import re
import sys
start =int(sys.argv[1])
end = int(sys.argv[2])
pat = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match and int(match.group('hour') >= start and int(match.group('hour') <= end:
        print '%s\t%s\t%s' % (match.group('ip') , match.group('hour'), 1)
