#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : Weibin Meng
# * Email         : m_weibin@163.com
# * Create time   : 2018-07-18 14:53
# * Last modified : 2018-07-22 13:09
# * Filename      : orderWords.py
# * Description   :
'''
'''
# **********************************************************


import os
import re
from ft_tree import getMsgFromNewSyslog

rawlog='../env-itsm-was-systemout0603.log'
templates='./out_logTemplate.txt'
sequences='./out_logSequence.txt'
order_templates='./out_logTemplate_order.txt'

tag_index={}
index_tag={}
tag_temp={}
tag_log={}

index=0
with open(sequences) as IN:
	for line in IN:
		tag=line.strip().split()[1]
		if tag not in tag_index:
			tag_index[tag]=index
			index_tag[index]=tag
		index+=1

index=0
with open(rawlog) as IN:
	for line in IN:
		if index in index_tag:
                        tag_log[index_tag[index]]=line.strip()
		index+=1

tag=1
with open(templates) as IN:
	for line in IN:
		tag_temp[str(tag)]=line.strip()
		tag+=1


# print len(tag_temp)
# print len(tag_log)
f=file(order_templates,'w')
for i in range(len(tag_temp)):
    tag=str(i+1)
    out=' '.join(list(set(tag_temp[tag].split())))
    if tag in tag_log:
        log=getMsgFromNewSyslog(tag_log[tag])[1]
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
        out=' '.join(new_temp)
    f.writelines(out+'\n')

print 'ordered'










