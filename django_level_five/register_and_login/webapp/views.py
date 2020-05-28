from django.shortcuts import render
from webapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'webapp/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form= UserProfileInfoForm()
    return render(request,'webapp/register.html',{'user':user_form,'profile':profile_form,'registered':registered})

def login(request):
    active = False
    if request.method == "POST":
        user_status = authenticate(username = request.POST['username'], password= request.POST['password'])
        if user_status:
            login(request,user)
            return HttpResponseRedirect(reverse('index',{'active':active}))
    return render(request,'webapp/login.html',{'active':active})

def other(request):
    return render(request,'webapp/other.html')
