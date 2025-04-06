#!/bin/bash

echo "Starting Dentify-AI"
# git pull
source ./env/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver