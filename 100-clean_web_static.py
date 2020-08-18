#!/usr/bin/python3
"""Create a .tgz file"""
from fabric.api import *
import datetime
import os
from os.path import isfile


def do_pack():
    """Create a .tgz file"""
    try:

        local("mkdir -p versions")
        fecha = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        nombre = "versions/web_static_" + fecha + ".tgz"
        local("tar -cvzf " + nombre + " web_static")
        print("web_static packed: {} -> {}Bytes".format(
            nombre, os.path.getsize(nombre)))
        return nombre
    except:
        return None

env.hosts = ['34.74.192.152', '35.237.243.141']


def do_deploy(archive_path):
    """deploys the
    """
    if isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        tmp_path = "/tmp/" + pre_path
        releases_path = "/data/web_static/releases/" + pre_path.split(".")[0]
        sudo("mkdir -p {:s}".format(releases_path))
        sudo("tar -xzf {:s} -C {:s}".format(tmp_path, releases_path))
        sudo("rm {:s}".format(tmp_path))
        all_path_w = releases_path + "/web_static/*"
        dictory_path = releases_path + "/web_static/"
        sudo("mv {:s} {:s}".format(all_path_w, releases_path))
        sudo("rm -rf {:s}".format(dictory_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    else:
        return False


def deploy():
    """deploy"""
    dreturn = do_pack()
    if dreturn is None:
        return False

    return do_deploy(dreturn)


def do_clean(number=0):
    """clean """
    num = int(number)
    if num <= 1:
        num = 1
    else:
        num += 1
        with lcd("versions"):
            local("ls -1t | tail -n +{:d} | xargs rm -rf".format(num))
        with cd("/data/web_static/releases/"):
            sudo("ls -1t -I test | tail -n +{:d} | xargs rm -rf".format(num))
