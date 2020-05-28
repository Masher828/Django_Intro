from django.urls import path
from webapp import views
app_name = 'webapp'

urlpatterns=[
    path ('',views.index,name="index"),
    path('register/',views.register,name ="register"),
    path('login/',views.login,name = "login"),
    path('other/',views.other,name = "other"),
]
