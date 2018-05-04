from django.conf.urls import url
from . import  views
from .views import classes,teachers,students,ajax

app_name = 'app01'
urlpatterns = [
    # url(r''),
    url(r'^$', classes.get_classes),
    url(r'^classes/', classes.get_classes),
    url(r'^add_classes/', classes.add_classes),
    url(r'^del_classes/', classes.del_classes),
    url(r'^edit_classes/', classes.edit_classes),

    url(r'^students/', students.get_students),
    url(r'^add_students/', students.add_students),
    url(r'^del_students/', students.del_students),
    url(r'^edit_students/', students.edit_students),

    url(r'^set_teachers/$', classes.set_teachers),

    url(r'ajax1/$', ajax.ajax1),
    url(r'ajax2/$', ajax.ajax2),
    url(r'ajax4/$', ajax.ajax4),
]