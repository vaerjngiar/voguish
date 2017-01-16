from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.ServicesView.as_view(), name='services')
]