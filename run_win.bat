@echo off
if not exist "venv\Scripts\activate" (
    echo Virtual enviroment didn't find. Creating...
    python -m venv venv
)

call venv\Scripts\activate


if exist "requirements.txt" (
    echo install requirements...
    pip install -r requirements.txt
)


echo execute collectstatic...
python manage.py collectstatic --noinput


echo Start the server
python manage.py runserver

deactivate