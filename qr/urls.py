"""
URL configuration for qr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path

from authorization.views import render_auth
from contacts.views import render_contacts
from gen_qr.views import render_gen_qr
from home.views import render_home
from my_qr.views import render_my_qr
from reg.views import render_reg
from settings.views import render_settings, render_card

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', render_home, name='home'),
    path('', render_home),
    path('auth/', render_auth, name='auth'),
    path('contacts/', render_contacts, name='contacts'),
    path('gen/', render_gen_qr, name='gen'),
    path('myqr/', render_my_qr, name='my_qr'),
    path('reg/', render_reg, name='reg'),
    path('settings/', render_settings, name='settings'),
    path('settings/card/', render_card, name='card'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)