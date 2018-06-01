# coding: utf-8
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
from DjangoUeditor.models import UEditorField

class Blog(models.Model):
	Name= models.CharField(max_length=100,blank=True)
	Content=UEditorField('内容',width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},
                         settings={},command=None, blank=True)

class Article(models.Model):
    title = models.CharField("博客标题", max_length=100)
    category = models.CharField("博客标签", max_length=50, blank=True)
    pub_date = models.DateTimeField("发布日期", auto_now_add=True, editable=True)
    update_time = models.DateTimeField("更细时间", auto_now=True,null=True)
    # content = models.TextField(blank=True, null=True)
    content = UEditorField("文章正文", height=300, width=1000, default="", blank=True, imagePath="uploads/blog02/images/",
                           toolbars="full", filePath="uploads/blog02/files/")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date',]
        verbose_name = "文章"
        verbose_name_plural = "文章"
