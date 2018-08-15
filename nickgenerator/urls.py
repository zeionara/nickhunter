from django.urls import path

from . import views

app_name = "nickgenerator"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug:nick_title>', views.details, name = 'nick'),
    path('like/<slug:nick_title>', views.like, name = 'like')
]
