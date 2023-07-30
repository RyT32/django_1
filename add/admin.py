from django.contrib import admin
# from .models import Test
from .models import Advertisement
# импортирую класс для подсказок 
from django.db.models.query import QuerySet


#  admin_class - класс для кастомизации
class AdvertisementAdmin(admin.ModelAdmin):
   # отображение в витде таблицы
   list_display = ['id','title','description','price','auction','created_at']  
   # параметры фильтрации
   list_filter = ['auction', 'created_at']
   #добавляю функции  лдля выбранных записей
   actions = ['make_auction_as_false']

   @admin.action(description='Убрать возможность торга')
   def make_auction_as_false(self,request,queryset:QuerySet):

      queryset.update(auction = False)
   # 18:42 - 18:52 






# подключаю модель
admin.site.register(Advertisement, AdvertisementAdmin)



# admin.site.register(Test)

# py manage.py createsuperuser - создание аккаунта админа
# (вводин имя почту и пароль   ! пароль не отображается )
# http://127.0.0.1:8000/admin