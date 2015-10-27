#!/usr/bin/python

import os

dict = {}
for d, fd, fl in os.walk('goagent-goagent-546de84/'):
        for f in fl:
                sufix = os.path.splitext(f)[1][1:]
                if dict.has_key(sufix):
                        dict[sufix] += 1
                else:
                        dict[sufix] = 1

for item in dict.items():
        print "%s : %s" % item
