sudo ln -s etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 hello:app
cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application
cd ..
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database qa;"
sudo mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'django'@'localhost';"
python3 ask/manage.py makemigrations
python3 ask/manage.py migrate