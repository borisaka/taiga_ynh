cd $install_path
git clone https://github.com/taigaio/taiga-events.git taiga-events
cd taiga-events
apt-get install -y nodejs nodejs-legacy npm
npm install
npm install -g coffee-script

cd $start_point
mkdir -p /var/log/taiga
cp ../conf/nginx.conf /etc/nginx/conf.d/$domain.d/$app.conf
cp ../conf/circus.service /etc/systemd/system/circus.service
systemctl daemon-reload
yunohost service add circus
yunohost service add rabbitmq
yunohost service add redis-server
yunohost service add postgresql
service circus start
service nginx reload
