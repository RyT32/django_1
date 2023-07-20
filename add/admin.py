from django.contrib import admin
from .models import Test



admin.site.register(Test)

# py manage.py createsuperuser - создание аккаунта админа
# (вводин имя почту и пароль   ! пароль не отображается )