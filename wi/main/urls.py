from django.urls import path
from django.contrib.auth.decorators import login_required # требует авторизацию
from .views import main_page

urlpatterns = [
    path('', login_required(main_page), name='main_page'),  # декоратор login_required
]
