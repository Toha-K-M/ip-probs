import os
this_folder = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(this_folder,'log')

import check
total = 0
infoCount = {}
with open(filename, 'r') as file:
    for line in file:
        if '[ERROR]' in line:
            total += 1
            check.checking(line)
        elif '[INFO]' in line:
            total += 1
            key = check.host(line)
            if key not in infoCount:
                infoCount[key] = 1
            else:
                infoCount[key] += 1

check.display(total,infoCount)
