from django.shortcuts import render # type: ignore
from . import models
# Create your views here.

def home(request):
    context = {
        'title':'Qizz',
        'sauces': models.Sauce.objects.all(),
        'toppings': models.Topping.objects.all(),
        'cakes': models.Cake.objects.all(),
    }
    return render(request, 'creamsQuizz/home.html', context=context)