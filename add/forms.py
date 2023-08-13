from django import forms


#widget нужен Для настройки над полями html
class AdvertisementForm(forms.Form):
    title =         forms.CharField(max_length=100) 
    description =   forms.CharField(widget=forms.Textarea()) # чтобы сделать многострочное поле нужно использовать виджет Textarea
    price =         forms.DecimalField()
    auction =       forms.BooleanField(required=False) # необязательное поле
    image =         forms.ImageField()
