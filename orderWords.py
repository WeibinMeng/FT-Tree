#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : Weibin Meng, Yuqing Liu
# * Email         : m_weibin@163.com
# * Create time   : 2018-07-18 14:53
# * Last modified : 2019-01-23 21:35
# * Filename      : orderWords.py
# * Description   :
'''
'''
# **********************************************************


import os
import re
from ft_tree import getMsgFromNewSyslog

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-templates', help='templates', type=str, default="./output.template")
parser.add_argument('-sequences', help='sequences', type=str, default="./output.seq")
parser.add_argument('-rawlog', help='rawlog', type=str, default="./training.log")
parser.add_argument('-order_templates', help='rawlog', type=str, default="./output.template_order")
args = parser.parse_args()


rawlog = args.rawlog
templates = args.templates
sequences = args.sequences
order_templates = args.order_templates

tag_index={}
index_tag={}
tag_temp={}
tag_log={}

index=0
with open(sequences) as IN:
    for line in IN:
        tag = line.strip().split()[1]
        # print(tag)
        if tag not in tag_index:
            #print(tag)
            tag_index[tag]=index
            index_tag[index]=tag
        index+=1

# if(tag_index):
#     print('tag_index-------------------------------')
#     for k, v in tag_index.items():
#         print(k, v)
# if(index_tag):
#     print('index_tag--------------------------------')
#     for k, v in index_tag.items():
#         print(k, v)
index=0
with open(rawlog) as IN:
    for line in IN:
        if index in index_tag:
            tag_log[index_tag[index]]=line.strip()
        index+=1
# if(tag_log):
#     print('tag_log-------------------------------')
#     for k, v in tag_log.items():
#         print(k, v)
tag=1
with open(templates) as IN:
    for line in IN:
        tag_temp[str(tag)]=line.strip()
        tag+=1
# if(tag_temp):
#     print('tag_temp-------------------------------')
#     for k, v in tag_temp.items():
#         print(k, v)

# print len(tag_temp)
# print len(tag_log)
f=open(order_templates,'w')
for i in range(len(tag_temp)):
    tag=str(i+1)
    out=' '.join(list(set(tag_temp[tag].split())))
    if tag in tag_log:
        # find the correspondent raw log
        log=getMsgFromNewSyslog(tag_log[tag])[1]
        # find the correspondent template
        temp=tag_temp[tag].split()
        new_temp=[]
        for k in log :
            # if i==len(tag_temp)-1:
            #     print log
            #     print temp
            #     print ''
            if k in temp:
                new_temp.append(k)
                temp.remove(k)
        # modify the template
        out=' '.join(new_temp)
    f.writelines(out+'\n')

print('ordered')









