db_user=$app
db_password=$app
db_name=$app


sudo -u postgres psql -a -f './_create_user.sql'
sudo -u postgres createdb $db_name -O $db_user

cd $install_path
git clone https://github.com/taigaio/taiga-back.git taiga-back
cd taiga-back
git checkout stable


source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3.4 taiga
pip install -r requirements.txt

# LDAP Auth
pip install taiga-contrib-ldap-auth
pip2 install circus
cd $start_point
mkdir -p /var/www/taiga/taiga-back/conf
cp ../conf/circus.ini /var/www/taiga/taiga-back/conf
cp ../conf/local.py /var/www/taiga/taiga-back/settings
# ga services

cd $install_path/taiga-back
python manage.py migrate --noinput
python manage.py compilemessages
python manage.py collectstatic --noinput

# Rabbit MQ for taiga
rabbitmqctl add_user taiga taiga
rabbitmqctl add_vhost taiga-celery
rabbitmqctl add_vhost taiga-events
rabbitmqctl set_permissions -p taiga-celerty taiga ".*" ".*" ".*"
rabbitmqctl set_permissions -p taiga-events taiga ".*" ".*" ".*"
