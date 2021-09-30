from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

# admin field order change

class QuestionAdmin(admin.ModelAdmin):
  fields = ['pub_date' , 'question_text']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

