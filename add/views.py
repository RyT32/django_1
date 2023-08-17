from django.shortcuts import render,redirect # redirect - переадресация 
from django.urls import reverse # получение ссылки полной по название в urls

from django.core.handlers.wsgi import WSGIRequest

from .models import Advertisement
from .forms import AdvertisementForm


# функции-представления
# <!-- {{}}  - это переменная -->
# <!-- {% %}  - это блоки с функционалом -->
# <!-- {% if else while for %}  - это блоки с функционалом -->

def home(request):
    data = Advertisement.objects.all() # беру все записи из БД
    context = {'advertisements' : data} # словарь
    return render(request, 'index.html', context)





    
def post_adv(request: WSGIRequest):
    
    print('request.GET',request.GET)
    print('request.POST',request.POST)
    print('request.FILES',request.FILES)
    print('request.user',request.user)

    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES) # передаю данные с запроса на проверку 
        if form.is_valid(): # True/False  проверяю правильность
            # print(request.POST['title'])
            print(form.cleaned_data) # отдает словарь со всеми данными
            adv = Advertisement(**form.cleaned_data) # распаковка словаря
            adv.user = request.user # отдельно указал пользователя 
            adv.save()  # сохраняю запись
            return redirect(
                reverse('home') # переадресация на главную страницу 
            )

        else: # если неправильно
            print(form.errors) # вывожу эту ошибку


    else: # GET или другие
        form = AdvertisementForm() # пустая форма

    context = {'form' : form} # словарь
    return render(request, 'advertisement-post.html', context)

# you.com/user
# get - получения всех пользоватлей
# post - добавление 
# put - обновление
# delete - удаление






def top_sellers(request):
    return render(request, 'top-sellers.html')



def test(request):
    return render(request, 'test.html')

def test2(request):
    return render(request, 'test2.html')




# testty = WSGIRequest()
# testty.content_params
# testty.path 

def test3(request : WSGIRequest):
    print("request : " , request.content_params )
    print("request : " , request.body )
    print("request : " , request.path )
    print("request : " , request.user )




    return render(request, 'test3.html')



# def func(x : list):
#     x.append


# func([1,2,3,4,5])


# def f(x,y):
#     print(x,y)

# r = {'x':1, 'y':2}
# f(x = r['x'], y = r['y'])
# f(**r)




