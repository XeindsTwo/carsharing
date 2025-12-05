from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CreateUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')