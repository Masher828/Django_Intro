from django.shortcuts import render
from .models import users
# Create your views here.
def index(request):
    return render (request,'db_forms/index.html')

def formpage(request):
    error = {"email_error": ""}
    if request.method == 'POST':
        if not users.objects.get_or_create(firstname = request.POST['fname'],lastname=request.POST['lname'],email = request.POST['email'])[1] :
            error['email_error']="Email already exists"
            return render(request,'db_forms/formpage.html',error)
        else:
            error['email_error']=""
            return login(request)
    return render(request,'db_forms/formpage.html',error)

def login(request):
    return render(request,'db_forms/login.html')

def other(request):
    return render(request,'db_forms/other.html')
