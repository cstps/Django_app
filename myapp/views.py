from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
# Create your views here.

class MyView(View):
  def get(self, request):
    # 뷰 로직 작성
    return HttpResponse('result')


class AboutView(TemplateView):
  template_name  = "about.html"
