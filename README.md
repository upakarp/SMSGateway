# SMSGateway

A small SMSGateway Project which uses take mobile number along with message from user. It uses django rest framework to display them as an API. Then, celery is also used to schedule the message to send at a later time. 

# Dependencies

amqp==1.4.9
anyjson==0.3.3
billiard==3.3.0.23
celery==3.1.26.post2
certifi==2018.4.16
chardet==3.0.4
Django==1.11
django-celery==3.2.2
django-cors-headers==2.2.0
django-redis==4.9.0
django-rest-framework==0.1.0
djangorestframework==3.8.2
idna==2.6
kombu==3.0.37
pytz==2018.4
redis==2.10.6
requests==2.18.4
urllib3==1.22
vine==1.1.4

# Installation
$ git clone https://github.com/upakarp/SMSGateway.git
$ cd src
$ Create virtual environment at your desired path using python -m venv env_name
$ Activate virtual environment
$ python ./manage.py runserver
$ In your browser root url is localhost:8000/api
$ localhost:8000/api/dashboard provide all the routes.
