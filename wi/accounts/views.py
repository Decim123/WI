from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordResetForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView

class CustomPasswordResetView(TemplateView):
    template_name = 'registration/password_changer.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            group_number = form.cleaned_data['group_number']
            group = Group.objects.get(name=group_number)
            user = form.save(commit=False)
            user.save()
            user.groups.add(group)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('/main')  # Перенаправление на страницу 'main' после успешной регистрации
        else:
            print(form.errors)
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')  # Перенаправление на главную страницу после успешного входа
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

def password_changer_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Обработка логики восстановления пароля
            # В этом блоке отправка письмо с ссылкой для сброса пароля но пока не готово
            messages.success(request, 'Instructions for password reset have been sent to your email.')
            return redirect('main')  # Перенаправление на главную страницу после отправки инструкций тоже пока хер его знает на главную закрыт же доступ не авторизованным
        else:
            messages.error(request, 'Password reset failed. Please correct the errors below.')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_changer.html', {'form': form})
