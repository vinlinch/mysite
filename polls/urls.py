from django.conf.urls import url
from django.views.generic import DetailView, ListView
from polls.models import Question
from polls import views
from django.utils import timezone
#todo

app_name = 'polls'
urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Question.objects.order_by('-pub_date')[:5],
            #todo
            #  queryset=Question.objects.filter(pub_date__lte=timezone.now).order_by('-pub_date')[:5],
            context_object_name='latest_question_list',
            template_name='polls/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Question,
            template_name='polls/detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/result/$',
        DetailView.as_view(
            model=Question,
            template_name='polls/results.html'),
        name='results'),
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]