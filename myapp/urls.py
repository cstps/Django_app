
from django.urls import path
from myapp.views import MyView, AboutView
from django.views.generic import TemplateView

urlpatterns =[
  path('', MyView.as_view()),
  # path('about', AboutView.as_view()),
  path('about', TemplateView.as_view(template_name ="about.html")),
]