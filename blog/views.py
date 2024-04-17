from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
from . import fake
def home(request):
    #return HttpResponse('<h1>Home</h1>');
    _posts = fake.getRandomPost(10);
    context = {
        'title':'Home Page | Writely | Home ',
        'posts':_posts,
        'featuredLonger': _posts[0],
        'featuredPosts': fake.getRandomPost(3),
    }
    return render(request,'blog/home.html',context=context);

def about(request):
    return HttpResponse('<h1>About</h1>');
