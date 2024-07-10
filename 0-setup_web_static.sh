#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static

# Install Nginx if not present
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary directories with permissions
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link (overwriting if exists)
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update ownership to ubuntu user and group (recursive)
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
cat > /etc/nginx/sites-available/default <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
    }
}
EOF

# Restart Nginx
systemctl restart nginx
