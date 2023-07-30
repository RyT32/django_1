from django.contrib import admin
# from .models import Test
from .models import Advertisement

#  admin_class - класс для кастомизации
class AdvertisementAdmin(admin.ModelAdmin):
   list_display = ['id','title','description','price','auction','created_at'] 



# подключаю модель
admin.site.register(Advertisement, AdvertisementAdmin)



# admin.site.register(Test)

# py manage.py createsuperuser - создание аккаунта админа
# (вводин имя почту и пароль   ! пароль не отображается )
# http://127.0.0.1:8000/admin