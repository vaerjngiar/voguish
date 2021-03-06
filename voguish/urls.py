"""voguish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^home/', include('home.urls', namespace='home', app_name='home')),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^services/', TemplateView.as_view(template_name='services.html'), name='services'),
    #url(r'^services/', include('services.urls', namespace='services', app_name='services')),
    url(r'^contact/', include('contact.urls', namespace='contact', app_name='contact')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
