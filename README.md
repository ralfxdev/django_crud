# DJANGO REST API

_Template of an api made with django restframework_

## Starting 🚀

_These instructions will allow you to get a working copy of the project on your local machine for development and testing purposes._


### Installation 🔧

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

## Super User 📦

email: test@gmail.com

user: test

password: test12345

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/api/helloworld/

Método POST => ```{"name":"nombre"}```


## Built with 🛠️

_Python, Django, Rest Framework_

* [Python3.10](https://docs.python.org/3/) - Programming language
* [Django](https://docs.djangoproject.com/en/4.0/) - MVC architecture management framework
* [Rest Framework](https://www.django-rest-framework.org/) - Used to generate the API


⌨️ whit ❤️ by [RALFxDev](https://github.com/ralfxdev) 😊
