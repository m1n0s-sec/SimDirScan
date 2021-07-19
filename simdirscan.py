#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author：M1n0s

import  requests
import sys

url = sys.argv[1]
with open('dict.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        r = requests.get(url+line)
        if r.status_code == 200:
            print(r.url + '存在')
















