#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get -y update
    sudo apt-get -y install nginx

mkdir -p data
mkdir -p data/web_static/
mkdir -p data/web_static/releases/
mkdir -p data/web_static/shared/
mkdir -p data/web_static/releases/test/
touch  data/web_static/releases/test/index.html
file=data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<h1>Hola Mundo</h1>\n\t</body>\n</html>" > "$file"
ln -sf data/web_static/releases/test/ data/web_static/current

chown -R ubuntu:ubuntu /data/
sed -i "66 a\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
service nginx restart
