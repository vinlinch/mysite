from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse , Http404
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request, 'polls/index.html', context=context)

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     return Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question})
    # return HttpResponse("你正在查看的问题{0}".format(question_id))

def results(request, question_id):
    response = "你正在看问题{0}的结果"
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("你对{0}问题进行投票.".format(question_id))

