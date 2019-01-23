#!/bin/bash
# **********************************************************
# * Author        : Weibin Meng
# * Email         : m_weibin@163.com
# * Create time   : 2018-10-18 13:18
# * Last modified : 2019-01-15 20:24
# * Filename      : gg.sh
# * Description   : 
# **********************************************************
git pull origin master
git add .
git commit -m "$1"
git push origin master
