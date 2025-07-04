from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('result/<str:result>/',views.result,name='result'),
]