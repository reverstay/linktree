from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from blog import views as blog_views  # Caso precise importar suas views do blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
path('i18n/', include('django.conf.urls.i18n')),

    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL para registro de usuários
    path('register/', blog_views.register, name='register'),

    # Redireciona a URL raiz para /blog/
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]

# Adiciona as configurações de arquivos estáticos e de mídia apenas no modo DEBUG
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
