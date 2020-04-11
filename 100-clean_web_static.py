#!/usr/bin/python3
""" Deploys """
from fabric.api import *


env.hosts = ['35.237.42.19', '107.21.12.250']
env.user = "ubuntu"


def do_clean(number=0):
    """ Keep it Clean"""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
