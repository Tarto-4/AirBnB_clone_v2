#!/usr/bin/python3
"""Module with function to deploy a web_static archive to remote servers"""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['3.84.222.117', '34.207.253.96']  # Replace with your server IPs

def do_deploy(archive_path):
    """
    Deploys an archive to remote servers.
    
    Args:
        archive_path (str): Path to the archive file.
    
    Returns:
        True if deployment succeeds, else False.
    """

    if not exists(archive_path):
        return False

    file_name = archive_path.split("/")[-1]  
    no_ext_name = file_name.split(".")[0] 
    release_path = f"/data/web_static/releases/{no_ext_name}"

    try:
        # Upload and extract the archive to the server.
        put(archive_path, "/tmp/")
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{file_name} -C {release_path}")
        run(f"rm /tmp/{file_name}") 

        # Move files into the correct place
        run(f"mv {release_path}/web_static/* {release_path}/")
        run(f"rm -rf {release_path}/web_static") 

        # Update the symbolic link to point to the new release.
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {release_path} /data/web_static/current")

        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
