#!/usr/bin/python3
'''
This script generates a .tgz archive from the contents of web_static folder
'''


from fabric.api import *
import datetime


env.user = 'ubuntu'
env.hosts = ['35.153.93.173', 'web-01.chege.tech']


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


def do_deploy(archive_path):
    '''
    Function distributes an archive to servers
    '''
    '''
    First, breakdown path name
    '''
    file_path = archive_path.split("/")
    filename = file_path[-1]
    del file_path[-1]
    '''
    if file_name[0] == "/"
    '''
    directory = ""
    for item in file_path:
        directory += item
    file_exists = local("find "+directory+" -name "+filename, capture=True)
    if filename not in file_exists:
        return False
    else:
        with cd("/tmp"):
            put(archive_path, filename)
        f_name = filename.split(".")
        f_name = f_name[0]
        releases = "/data/web_static/releases/"
        sudo("mkdir -p "+releases+f_name)
        sudo("tar -xzf /tmp/"+filename+" -C /data/web_static/releases/"+f_name)
        sudo("rm /tmp/"+filename)
        sudo("mv "+releases+f_name+"/web_static/* "+releases+f_name)
        sudo("rm -rf /data/web_static/releases/"+f_name+"/web_static")
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s "+releases+f_name+"/ /data/web_static/current")
        print("New version deployed!")
