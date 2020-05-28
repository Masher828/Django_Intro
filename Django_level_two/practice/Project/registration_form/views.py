from django.shortcuts import render
from django.http import HttpResponse
from registration_form.models import user_details
# Create your views here.
def index(request):
    return render(request,'registration_form/index.html')


def user(request):
    data = user_details.objects.all()
    data_dict ={'user_details':data}
    return render(request,'registration_form/users.html',data_dict)
