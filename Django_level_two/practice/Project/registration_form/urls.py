from django.urls import path
from registration_form import views
urlpatterns=[
    path('', views.user),
]
