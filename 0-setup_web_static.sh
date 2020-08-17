#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if ! which nginx > /dev/null 2>&1; then
    echo "Nginx not installed"

else
    echo "Installed"
fi

sudo mkdir -p data
sudo mkdir -p data/web_static/
sudo mkdir -p data/web_static/releases/
sudo mkdir -p data/web_static/shared/
sudo mkdir -p data/web_static/releases/test/
sudo touch -p data/web_static/releases/test/index.html
file=/data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<h1>Hola Mundo</h1>\n\t</body>\n</html>" > "$file"

if [ [-L data/web_static/current] && [ -e data/web_static/current ]]; then
    echo "symbolic link exists"
else
    echo "symbolic links doesn't exists"
fi
# ln -s data/web_static/releases/test/ data/web_static/current 