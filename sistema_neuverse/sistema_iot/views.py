from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Adicionar esta linha
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Importe o novo formulário personalizado
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required  # Garante que apenas usuários logados podem acessar essa página
def home_view(request):
    # Aqui você pode buscar os dados que quer mostrar na página inicial, como notificações, feed, etc.
    return render(request, 'sistema_iot/home.html')

def index(request):
    theme = request.GET.get('theme')
    if theme:
        request.session['theme'] = theme
    theme = request.session.get('theme', 'light')
    return render(request, 'sistema_iot/index.html', {'theme': theme})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua conta foi criada com sucesso! Você já pode fazer login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sistema_iot/register.html', {'form': form})
