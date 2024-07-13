#!/usr/bin/env python3
"""
Fabric script (based on 1-pack_web_static.py) that distributes an archive
to web servers.
"""

from fabric.api import env, put, run, local
from os.path import exists


env.hosts = ['3.84.222.117', '34.207.253.96']  # Replace with your server IPs


def do_deploy(archive_path):
    """Distributes an archive to the web servers.

    Args:
        archive_path (str): The path to the archive file.

    Returns:
        bool: True if successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        file_name = archive_path.split("/")[-1]
        no_ext_name = file_name.split(".")[0]
        release_path = "/data/web_static/releases/{}/".format(no_ext_name)

        put(archive_path, "/tmp/")

        # Create the release directory
        run('mkdir -p {}'.format(release_path))

        # Uncompress the archive to the release directory
        run('tar -xzf /tmp/{} -C {}'.format(file_name, release_path))

        # Remove the archive from the /tmp/ directory
        run('rm -f /tmp/{}'.format(file_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link to the new version of the code
        run('ln -s {} /data/web_static/current'.format(release_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
