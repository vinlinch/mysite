from django.shortcuts import redirect
from django.shortcuts import render

from app01 import models


def get_classes(request):
    cls_lis = models.Classes.objects.all()
    return render(request, 'get_classes.html',{'cls_list':cls_lis})

def add_classes(request):
    if request.method == 'GET':
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title','')
        models.Classes.objects.create(titil=title)
        return redirect('/class.html')

def del_classes(request):
    nid = request.GET.get('nid','')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/class.html')

def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid','')
        obj = models.Classes.objects.get(id=nid)
        return render(request,'edit_classes.html',{'obj':obj})
    elif request.method == 'POST':
        nid = request.POST.get('nid','')
        title = request.POST.get('xxoo','')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes.html')

def set_teachers(request):
    if request.method == 'GET':
        nid = request.GET.get('nid', '')
        cls_obj = models.Classes.objects.get(id=nid)
        cls_teacher_list = cls_obj.all()
        all_teacher_list = models.Teachers.objects.all()
        return render(request, 'set_teachers.html',{
            'cls_teacher_list':cls_teacher_list,
            'all_teacher_list':all_teacher_list,
            'nid':nid,
        })
    elif request.method =='POST':
        nid = request.POST.get('nid', '')
        ids_str = request.POST.getlist('teacher_id','')
        ids_int = []
        for i in ids_str:
            i = int(i)
            ids_int.append(i)
        obj = models.Classes.objects.get(id=nid)
        obj.a.set(ids_int)
        return redirect('/classes.html')