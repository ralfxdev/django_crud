# DJANGO REST API

_Template of an api made with django restframework_

## Starting ð

_These instructions will allow you to get a working copy of the project on your local machine for development and testing purposes._


### Installation ð§

_Follow each of the steps for the installation_


```
python3 -m venv env

env\Scripts\Activate  powershell => .ps1  cmd => .bat

pip install -r requirements.txt

django-admin startproject proyecto_api

cd proyecto_api

python manage.py startapp Api

python manage.py makemigrations Api

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 
```

## Super User ð¦

email: test@gmail.com

user: test

password: test12345

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/api/helloworld/

http://127.0.0.1:8000/api/botellas/

http://127.0.0.1:8000/api/cervezas/

MÃ©todo POST => ```{"name":"nombre"}```


## Built with ð ï¸

_Python, Django, Rest Framework_

* [Python3.10](https://docs.python.org/3/) - Programming language
* [Django](https://docs.djangoproject.com/en/4.0/) - MVC architecture management framework
* [Rest Framework](https://www.django-rest-framework.org/) - Used to generate the API


â¨ï¸ whit â¤ï¸ by [RALFxDev](https://github.com/ralfxdev) ð
