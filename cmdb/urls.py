from django.conf.urls import url
from . import  views

app_name = 'cmdb'
urlpatterns = [
    url(r'^$',views.index),
]