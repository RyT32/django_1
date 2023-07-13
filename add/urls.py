from django.urls import path

# импортирую свои представления

from .views import home, test, test2, top_sellers

#  маршрутизатор приложения




urlpatterns = [
    path("", home, name = 'home'), # главная страница 
    path("top_sellers", top_sellers, name='top_sellers'), # топ продавцов 
    path("test/", test, name = 'test'), 
    path("test2/", test2, name = 'test2'), 
]   
