
from django.urls import path,include
from App import views

urlpatterns=[
    path('',views.help,name="help"),
    path('myext/',views.myext, name='myext'),

]
