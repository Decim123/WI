from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
