#!/usr/bin/env bash

sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y python-pip
sudo apt-get install -y python-software-properties
sudo apt-get install -y python3.4
sudo apt-get install -y python3.4-dev
sudo pip install virtualenv
sudo apt-get install -y apache2
rm -rf /var/www
ln -fs /vagrant /var/www
cd /vagrant
virtualenv --unzip-setuptools --python=/usr/bin/python3.4 .
source bin/activate
pip install -r requirements.txt
python manage.py runserver