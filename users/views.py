from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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
