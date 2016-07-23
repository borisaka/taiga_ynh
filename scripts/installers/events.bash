cd $install_path
git clone https://github.com/taigaio/taiga-events.git taiga-events
cd taiga-events
apt-get install -y nodejs nodejs-legacy npm
npm install
npm install -g coffee-script
