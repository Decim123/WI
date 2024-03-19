from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    group_number = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('email', 'group_number', 'password1', 'password2')  # Удаляем поле 'username' из списка полей

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            self.fields['username'].required = False  # Делаем поле 'username' необязательным

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Присваиваем значение email полю username
        if commit:
            user.save()
        return user
