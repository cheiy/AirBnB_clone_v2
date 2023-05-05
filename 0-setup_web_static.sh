#!/usr/bin/env bash
# Bash script prepares servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Sam's content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu -R /data/
sudo sed -i '56i \\tlocation \/hbnb_static\/ {' /etc/nginx/sites-enabled/default
sudo sed -i '57i \\t\talias \/data\/web_static\/current\/;' /etc/nginx/sites-enabled/default
sudo sed -i '58i \\t\tautoindex off;' /etc/nginx/sites-enabled/default
sudo sed -i '59i \\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart
sudo service nginx start
