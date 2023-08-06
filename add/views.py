from django.shortcuts import render # для того чтобы отдавать html

from .models import Advertisement


# функции-представления
# <!-- {{}}  - это переменная -->
# <!-- {% %}  - это блоки с функционалом -->
# <!-- {% if else while for %}  - это блоки с функционалом -->

def home(request):
    data = Advertisement.objects.all() # беру все записи из БД
    context = {'advertisements' : data} # словарь
    return render(request, 'index.html', context)




def top_sellers(request):
    return render(request, 'top-sellers.html')



def test(request):
    return render(request, 'test.html')

def test2(request):
    return render(request, 'test2.html')


from django.core.handlers.wsgi import WSGIRequest


# testty = WSGIRequest()
# testty.content_params
# testty.path 

def test3(request : WSGIRequest):
    print("request : " , request.content_params )
    print("request : " , request.body )
    print("request : " , request.path )
    print("request : " , request.user )




    return render(request, 'test3.html')