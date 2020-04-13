from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.member_form),
    path('list/', views.member_list)
    ]