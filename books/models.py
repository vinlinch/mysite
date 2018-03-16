# -*- coding utf-8 -*-
from django.db import models
from django.contrib import admin

# Create your models here.
#先设计作者Author对象(表)
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField() #email字段,使用email自带的格式

    def __unicode__(self):#定义unicode函数,是为了让对象在实例化的时候,可以返回打印输出它的名字
        return "%s--%s" %(self.first_name,self.last_name)

# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=64, unique=True) #出版社名称,唯一,是主键
    address = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=32)
    state_province = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    website = models.URLField() #主页,采用自带的url格式

    def __unicode__(self):
        return "%s" % (self.name)

#定义一个选项,里面包含3个可选框,用以下面的书籍表publisher_state下拉选择
STATUS_CHOICE =(
    ('checkout', u'已出版'),
    ('dai',u'待出版'),
    ('status',u'审核中'),
)

class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ManyToManyField(Author) #作者,多对多的关系
    publisher = models.ForeignKey(Publisher) #出版社,外键管理到Publisher表
    publisher_date = models.DateField(auto_now_add=True)
    publisher_state = models.CharField(max_length=20, choices=STATUS_CHOICE,default='checkout')

    def __unicode__(self):
        return "%s--%s" %(self.name,self.publisher_date)
