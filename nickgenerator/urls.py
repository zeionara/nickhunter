from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug:nick_title>', views.details, name = 'nick')
]
