from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.

def home(request):
    return HttpResponse('<h1>Home</h1>');
def about(request):
    return HttpResponse('<h1>About</h1>');