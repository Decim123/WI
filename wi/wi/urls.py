from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register
from accounts.views import CustomPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('', RedirectView.as_view(url='/main/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),  # встроенные URL-шаблоны для аутентификации Django
    path('register/', register, name='register'),
    path('password_changer/', CustomPasswordResetView.as_view(), name='password_changer'),  # добавленный путь для страницы восстановления пароля
]

# Обработка статических файлов
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
