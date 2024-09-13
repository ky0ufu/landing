#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Virtual enviroment didn't find. Creating..."
    python3 -m venv venv
fi


source venv/bin/activate


if [ -f "requirements.txt" ]; then
    echo "install requirements..."
    pip install -r requirements.txt
fi


echo "execute collectstatic..."
python3 manage.py collectstatic --noinput


echo "Start up the server"
python3 manage.py runserver


deactivate