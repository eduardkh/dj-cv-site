# Initial Steps

## Initiate git

`git init`

## Create a virtual environment and install django


```
pipenv install pep8 --dev
pipenv install autopep8 --dev
pipenv shell
pip install django
pip freeze > requirements.txt (optional)
```

## Install requirements (optional)

`pip install -r requirements.txt`

## Create Project
```
django-admin startproject rpi
cd rpi
```
## Check the server for the first time
```
manage.py migrate
manage.py runserver
```
## Create App
```
django-admin startapp cv
```
## Create super-user
```
manage.py createsuperuser
```
## Sync model to the database
```
manage.py makemigrations
manage.py migrate
```