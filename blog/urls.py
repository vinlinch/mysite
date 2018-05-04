from django.conf.urls import url
from . import views
app_name = 'blogs'
urlpatterns = [
    url(r'^$', views.archive),
    url(r'blogs/$', views.archive),
    url(r'blog/$', views.blog_index),
]
