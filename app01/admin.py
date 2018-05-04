from django.contrib import admin
from app01 import models
# Register your models here.

#配置出版社的扩展显示
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('title',)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('username','age',)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Classes, ClassesAdmin)
admin.site.register(models.Students, StudentsAdmin)
admin.site.register(models.Teachers, TeachersAdmin)