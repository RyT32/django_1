from django.shortcuts import render,redirect # redirect - переадресация 
from django.urls import reverse # получение ссылки полной по название в urls

from django.core.handlers.wsgi import WSGIRequest

from .models import Advertisement
from .forms import AdvertisementForm

from django.contrib.auth import get_user_model # получаем модель пользователей
from django.db.models import Count # для подсчета 

User = get_user_model()

# функции-представления
# <!-- {{}}  - это переменная -->
# <!-- {% %}  - это блоки с функционалом -->
# <!-- {% if else while for %}  - это блоки с функционалом -->

def home(request: WSGIRequest):
    title = request.GET.get('query')
    if title: # если пользователь что-то ищет
        data = Advertisement.objects.filter(title__icontains = title) # SELECT * FROM Advertisement WHERE title = title
    else: # если ничего не ищет(просто все обьявления)
        data = Advertisement.objects.all() # беру все записи из БД
    context = {'advertisements' : data, 'title': title} # словарь
    return render(request, 'index.html', context)



def top_sellers(request):
    users = User.objects.annotate(
        adv_count = Count('advertisement')# записываю в  adv_count колисчество обьявлений у каждого пользователя
    ).order_by('-adv_count') # сортировка от наибольшего к наименьшему

    context = {"users" : users}
    return render(request, 'top-sellers.html', context)






def post_adv_detail(request: WSGIRequest, pk):
    # post_adv/<int:pk>/
    # http://127.0.0.1:8000/post_adv/1/
    # pk = 1
    adv = Advertisement.objects.get(id = pk) # ищу запись по id
    context = {"adv" : adv}
    return render(request, 'advertisement.html', context)





    
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




# py manage.py shell   
# from add.models import Advertisement
### WHERE
### number
# adv = Advertisement.objects.filter(price__lt = 100) # lt  <
# adv = Advertisement.objects.filter(price__gt = 100) # gt  >
# adv = Advertisement.objects.filter(price__lte = 100) # lte  <=
# adv = Advertisement.objects.filter(price__gte = 100) # gte  >=

### string
# adv = Advertisement.objects.filter(title__contains = 'мол') # ищет данную строку в названиях чувствителен к регистру ("мол" in title)
# ##работает только для английского языка
# adv = Advertisement.objects.filter(title__icontains = 'мол') # ищет данную строку в названиях не чувствителен к регистру ("мол".lower() in title.lower())


# adv = Advertisement.objects.filter(title__startswith = 'Мол') # ищет данную строку в начале названия
# adv = Advertisement.objects.filter(title__endswith = 'ко') # ищет данную строку в конце названия
# adv = Advertisement.objects.filter(title__istartswith = 'Мол') # ищет данную строку в начале названия
# adv = Advertisement.objects.filter(title__iendswith = 'ко') # ищет данную строку в конце названия

# from django.db import connection
# connection.queries







