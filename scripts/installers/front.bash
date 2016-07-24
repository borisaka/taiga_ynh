cd $install_path
git clone https://github.com/taigaio/taiga-front-dist.git taiga-front-dist
cd taiga-front-dist
git checkout stable
cd $start_point
cp ../conf/taiga-front.json /var/www/taiga/taiga-front-dist/dist/conf.json
