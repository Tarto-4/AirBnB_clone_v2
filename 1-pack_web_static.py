#!/usr/bin/python3
"""Module with function to pack web_static files into a tgz archive"""

from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """
    Creates a tgz archive from the contents of the web_static folder.
    
    Returns:
        The path of the archive if successful, else None.
    """
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = f"versions/web_static_{now}.tgz"
        local("mkdir -p versions")  # Create versions dir if not exists
        local(f"tar -cvzf {archive_path} web_static")
        return archive_path
    except Exception:
        return None
