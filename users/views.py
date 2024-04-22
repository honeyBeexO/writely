from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            print(f'{username}')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})
    