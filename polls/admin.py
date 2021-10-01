from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice



# admin field order change

class ChoiceInline(admin.TabularInline):
      model = Choice
      extra = 2


class QuestionAdmin(admin.ModelAdmin):
      fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
      ]
      inlines = [ChoiceInline]
      list_display = ('question_text','pub_date') # 제목과 칼럼 추가
      list_filter = [ 'pub_date'] # 필터창 추가
      search_fields = ['question_text'] # 검색박스 추가



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

