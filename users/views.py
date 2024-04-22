from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Account was successfully registered for {username}')
            return redirect('blog-home')
        else:
            print(f'Registration failed: {form.errors}')
            messages.error(request, f'Account creation failed')

    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})
    