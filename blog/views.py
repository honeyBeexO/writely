from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
from blog.models import Post
def home(request):
    #return HttpResponse('<h1>Home</h1>');
    _posts = Post.objects.all()
    context = {
        'title':'Home Page | Writely | Home ',
        'posts':_posts[3:],
        'featuredLonger': _posts[0],
        'featuredPosts': _posts[:3],
    }
    return render(request,'blog/home.html',context=context);

def about(request):
    return HttpResponse("<h1>About</h1>");
