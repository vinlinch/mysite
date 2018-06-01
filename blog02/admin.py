from django.contrib import admin
from .models import Article, Blog
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Article )
admin.site.register(Blog)