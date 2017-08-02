from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^$', views.items, name = 'items'),
    url(r'^$', views.services, name = 'services'),
    url(r'^$', views.look, name = 'gallery'),

]