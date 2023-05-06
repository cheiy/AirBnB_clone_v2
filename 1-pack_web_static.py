#!/usr/bin/python3
'''
This script generates a .tgz archive from the contents of web_static folder
'''


from fabric.api import *
import datetime


def do_pack():
    '''
    Function compresses folder to .tgz
    '''
    now = datetime.datetime.now()
    local('mkdir -p versions')
    yr = str(now.year)
    mn = str(now.month)
    day = str(now.day)
    H = str(now.hour)
    M = str(now.minute)
    S = str(now.second)
    our_date = yr+mn+day+H+M+S
    res = local("tar -cvzf  versions/web_static_"+our_date+".tgz web_static")
    if res.failed is False:
        fsize = local('ls -s versions/web_static_' + our_date + '.tgz',
                      capture=True)
        fsize = fsize.partition(" ")
        fsize = fsize[0]
        print("web_static packed: versions/web_static_" + our_date + ".tgz\
              --> " + fsize + "Bytes")
