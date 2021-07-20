#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author：M1n0s

import sys
import math
import getopt
import threading
import requests

def init():
    print('''

   _____   _               _____    _           _____                        
  / ____| (_)             |  __ \  (_)         / ____|                       
 | (___    _   _ __ ___   | |  | |  _   _ __  | (___     ___    __ _   _ __  
  \___ \  | | | '_ ` _ \  | |  | | | | | '__|  \___ \   / __|  / _` | | '_ \ 
  ____) | | | | | | | | | | |__| | | | | |     ____) | | (__  | (_| | | | | |        
 |_____/  |_| |_| |_| |_| |_____/  |_| |_|    |_____/   \___|  \__,_| |_| |_| 
                                                                                     
                          Designed by M1n0s
                                 V1.0                                                                                                                                                                                                                                                                                      
    ''')
    print('******************************************************************************')
    print('This is a simple directory scanner!')
    print('About using it , for example:')
    print('python simdirscan.py -u URL -t THREADING -d DICTIONARY')
    print('******************************************************************************')

init()

def start():
    if(len(sys.argv) == 7):
        opts, args = getopt.getopt(sys.argv[1:], 'u:t:d:')
        for m,n in opts:
            if m == '-u':
                url = n
            elif m == '-t':
                threads = n
            elif m == '-d':
                dict = n
        mscan(url,threads,dict)
    else:
        print('There was an error in your operation.')

def mscan(url,threads,dict):
    result_list = []
    threads_list = []
    with open('dict.txt','r') as f:
        dic_list = f.readlines()
        if len(dic_list) % int(threads) == 0:
            thread_read_line_number = len(dic_list) / int(threads)
        else:
            thread_read_line_number = math.ceil(len(dic_list) / int(threads))
        i = 0
        temp_list = []
        for line in dic_list:
            i = i+1
            if i % thread_read_line_number == 0:
                temp_list.append(line.strip())
                result_list.append(temp_list)
                temp_list = []
            else:
                temp_list.append(line.strip())
    for i in result_list:
        threads_list.append(threading.Thread(target=scan, args=(url,i)))
    for t in threads_list:
        t.start()

def scan(url,dict):
    for line in dict:
        r = requests.get(url + '/' +line)
        if r.status_code == 200:
            print(r.url + '已扫描到' )
start()

