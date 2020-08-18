#!/usr/bin/python3
"""Create a .tgz file"""
from fabric.api import local
import datetime
import os


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
