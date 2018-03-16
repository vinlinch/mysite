from django.shortcuts import render
from django.shortcuts import redirect

from app01 import models

def get_students(request):
    stu_list = models.Students.objects.all()
    return render(request,'get_students.html',{'stu_list':stu_list})

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        return render(request, 'add_students.html', {'cs_list':cs_list})
    elif request.method == 'POST':
        u = request.POST.get('username','')
        a = request.POST.get('age','')
        g = request.POST.get('gender','')
        c = request.POST.get('cs','')
        models.Students.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_is=c
        )
        return redirect('/students.html')

def del_students(request):
    nid = request.GET.get('nid', '')
    models.Students.objects.filter(id=nid).delete()
    return redirect('/students.html')

def edit_students(request):
    if request.method == 'GET':
        nid = request.GET.get('nid', '')
        obj = models.Students.objects.get(nid)
        cs_list = models.Classes.objects.all()
        return render(request, 'edit_classes.html', {'obj':obj,'cs_list':cs_list})
    elif request.method == 'POST':
        nid = request.POST.get('nid', '')
        u = request.POST.get('username', '')
        a = request.POST.get('age', '')
        g = request.POST.get('gender', '')
        c = request.POST.get('cs','')
        models.Students.objects.filter(id=nide).update(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect('/students.html')