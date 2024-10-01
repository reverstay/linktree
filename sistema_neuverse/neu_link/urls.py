from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from sistema_iot import views as sistema_iot_views  # Importa suas views personalizadas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema_iot/', include('sistema_iot.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='sistema_iot/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL para registro de usuários usando a nova view personalizada
    path('register/', sistema_iot_views.register, name='register'),  # Usando a view personalizada de registro

    # Redireciona a URL raiz para /sistema_iot/
    path('', RedirectView.as_view(url='/sistema_iot/', permanent=True)),
]

# Configurações de arquivos estáticos no modo DEBUG
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
