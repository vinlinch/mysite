from django.contrib import admin
from polls import models
# Register your models here.
#

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    date_hierarchy = 'pub_date'


admin.site.register(models.Question, QuestionAdmin )
admin.site.register(models.Choice)