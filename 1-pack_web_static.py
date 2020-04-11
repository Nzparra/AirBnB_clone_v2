#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        tm = datetime.now()
        stamp = "%Y%m%d%H%M%S"
        file_path = 'versions/web_static_{}.tgz'.format(tm.strftime(stamp))
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path
    except:
        return None
