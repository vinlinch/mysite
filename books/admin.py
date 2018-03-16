# -*- coding utf-8 -*-
from django.contrib import admin
from books import models

# Register your models here.
# 创建一个Bookadmin的modeladmin的子类
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','publisher','publisher_date',)
    search_fields = ('name',)
    list_filter = ('publisher','publisher_date',)
    list_per_page = 5
    list_editable = ('name' ,)
    list_select_related = ('publisher',)
    filter_horizontal = ('author',)
    raw_id_fields = ('publisher',)
    actions = ['set_publisher_chekout','set_publisher_dai','set_publisher_status','set_publisher_del',]

    def set_publisher_checkout(modeladmin,request,queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='checkout')
    def set_publisher_dai(modeladmin,request,queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='dai')
    def set_publisher_status(modeladmin,request,queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='status')
    def set_publisher_del(modeladmin,request,queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).delete()

    set_publisher_checkout.short_description = "设置所有的数据为--已出版"
    set_publisher_status.short_description = "设置所有的书籍为--审核中"
    set_publisher_dai.short_description = "设置所有的书籍为--待出版"
    set_publisher_del.short_description = "设置所有的书籍为--删除"

#配置作者页面的扩展内容
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email')

#配置出版社的扩展显示
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','country',)


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Author, AuthorAdmin)