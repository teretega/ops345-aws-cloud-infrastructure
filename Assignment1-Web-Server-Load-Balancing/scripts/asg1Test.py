#!/usr/bin/env python3
# asg1Test.py
# Test for OPS345 Assignment 1
# Author: Andrew Smith
# Changes by: Oghenetega Clinton Tere

import os
import re
import time

end_time = time.time() + 60

numMain = 0
numSlave1 = 0
numSlave2 = 0
numSlave3 = 0

while time.time() < end_time:
    output = os.popen(
        "curl --no-progress-meter http://15.157.28.86/"
    ).read()

    ip = re.search(r'10\.3\.45\.\d+', output)

    if ip:
        if ip[0] == '10.3.45.11':
            numMain += 1
        elif ip[0] == '10.3.45.21':
            numSlave1 += 1
        elif ip[0] == '10.3.45.22':
            numSlave2 += 1
        elif ip[0] == '10.3.45.23':
            numSlave3 += 1

print('Hits on main www server: ' + str(numMain))
print('Hits on www-slave1 server: ' + str(numSlave1))
print('Hits on www-slave2 server: ' + str(numSlave2))
print('Hits on www-slave3 server: ' + str(numSlave3))