from django.urls import path
from db_forms import views
app_name = 'db_forms'
urlpatterns=[
    path('',views.index,name = "index"),
    path('/formpage',views.formpage,name = "formpage"),
    path('/other',views.other,name='other'),
]
