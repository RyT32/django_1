from django.contrib import admin

from .models import Advertisement # импортирую свою модель
from django.db.models.query import QuerySet

# py manage.py createsuperuser - создания аккаунта супер пользователя
# пароль не отображается
# http://127.0.0.1:8000/admin



# класс для кастомизации модели в админке
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','title','description','price','auction', 'created_date', 'update_date', 'photo' ] # столбцы для отображения в таблице
    list_filter = ['auction','created_at','price'] # столбцы по которым будет фильтрация
    actions = ['make_action_as_false','make_action_as_true'] # методы для выбюранных записей
    search_fields = ['title']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Общие', { # блок 1 
            "fields": (
                'title','description', 'user' , 'image'    # поля блока
            ),
        }),
        ('Финансы', { # блок 2
            "fields": (
                'price','auction'    # поля блока
            ),
            'classes': ['collapse'] # скрыть/показать блок
        })
    )
    


    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False) # обновить значение auction у выбранных записей на False


    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True) # обновить значение auction у выбранных записей на False








# подключение модели в админку и кастомной модели
admin.site.register(Advertisement, AdvertisementsAdmin)





# py manage.py createsuperuser - создание аккаунта админа
# (вводин имя почту и пароль   ! пароль не отображается )
# http://127.0.0.1:8000/admin