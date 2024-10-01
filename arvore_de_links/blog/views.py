from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    theme = request.GET.get('theme')
    if theme:
        request.session['theme'] = theme
    theme = request.session.get('theme', 'light')
    return render(request, 'blog/index.html', {'theme': theme})

def register(request):
    theme = request.session.get('theme', 'light')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form, 'theme': theme})

def login(request):
    theme = request.session.get('theme', 'light')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid login credentials', 'theme': theme})
    return render(request, 'blog/login.html', {'theme': theme})
