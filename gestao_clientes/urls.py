"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    Test
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as auth_views


#from .views import artigos, fname
from clientes import urls as clientes_urls
from home import urls as home_urls

urlpatterns = [
    #path('artigos/<int:year>/', artigos),
    #path('pessoa/<str:nome>/', fname),
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    # DECORATORRRRR AQUIIIIIIIIIIIIIIIIII
    #path('login/', auth_views.LoginView, name='login'),
    #path('logout/', auth_views.LogoutView, name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
