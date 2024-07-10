#!/usr/bin/env python3

"""
This script installs Nginx if it is not already installed,
creates necessary folders, creates a fake HTML file,
creates a symbolic link, gives ownership of the /data/ folder to the ubuntu user and group,
updates Nginx configuration, and restarts Nginx.
"""

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi
        apt-get update
        apt-get -y install nginx
fi

# Create necessary folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\tautoindex off;\n}' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart;