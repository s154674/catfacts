from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index')
]
