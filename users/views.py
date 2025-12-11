from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import CreateUserCreationForm

User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = CreateUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # сразу логиним нового пользователя
            return redirect('/') # редирект на главную страницу

    else:
        form = CreateUserCreationForm() # пустая форма для GET-запроса
    return render(request, 'register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # проверяем данные
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # авторизация прошла успешно
            login(request, user)
            return redirect('home')
        else:
            # ошибка входа
            messages.error(request, "Неверный логин или пароль")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')