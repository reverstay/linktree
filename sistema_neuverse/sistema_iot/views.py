from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Adicionar esta linha
from django.shortcuts import render, redirect

def index(request):
    theme = request.GET.get('theme')
    if theme:
        request.session['theme'] = theme
    theme = request.session.get('theme', 'light')
    return render(request, 'sistema_iot/index.html', {'theme': theme})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário
            messages.success(request, 'Sua conta foi criada com sucesso! Você já pode fazer login.')
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()  # Formulário vazio para GET
    return render(request, 'sistema_iot/register.html', {'form': form})
