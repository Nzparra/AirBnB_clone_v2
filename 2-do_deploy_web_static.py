#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import *
from datetime import datetime
import shlex
import os


env.hosts = ['35.237.42.19', '107.21.12.250']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy """
    if not os.path.exists(archive_path):
        return False
    try:
        n = archive_path.replace('/', ' ')
        n = shlex.split(n)
        n = n[-1]
        w = n.replace('.', ' ')
        w = shlex.split(w)
        w = w[0]
        release = "/data/web_static/releases/{}/".format(w)
        tmp = "/tmp/{}".format(n)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release))
        run("tar -xzf {} -C {}".format(tmp, release))
        run("rm {}".format(tmp))
        run("mv {}web_static/* {}".format(release, release))
        run("rm -rf {}web_static".format(release))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release))
        print("New version deployed!")
        return True
    except:
        return False
