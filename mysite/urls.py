"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from cmdb import views
from app01.views import classes,students,teachers, ajax
from blog import views as blog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index),

    url(r'^classes.html', classes.get_classes),
    url(r'^add_classes.html', classes.add_classes),
    url(r'^del_classes.html', classes.del_classes),
    url(r'^edit_classes.html', classes.edit_classes),

    url(r'^students.html', students.get_students),
    url(r'^add_students.html', students.add_students),
    url(r'^del_students.html', students.del_students),
    url(r'^edit_students.html', students.edit_students),

    url(r'^set_teachers.html', classes.set_teachers),

    url(r'^ajax1.html', ajax.ajax1),
    url(r'^ajax2.html', ajax.ajax2),
    url(r'^ajax4.html', ajax.ajax4),

    url(r'^blogs/', blog.archive)


]
