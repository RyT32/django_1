from django.shortcuts import render # для того чтобы отдавать html

# Create your views here.


# функции-представления

def home(request):
    return render(request, 'index.html')
