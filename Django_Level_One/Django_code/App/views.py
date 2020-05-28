from django.shortcuts import render
from django.http import HttpResponse
from App.models import Topic,Webpage,AccessRecord
# from django.template import loader
# Create your views here.
def index(request):

    return HttpResponse('<h1>Hello World I am inside App views.py and called through index view</h1>')

def help(request):
    webpages_list = AccessRecord.objects.all()
    date_dict = {'access_record':webpages_list}
    # help_dict = {'insert':"This is the help page "}
    return render(request,'App/help.html',date_dict)
    # template = loader.get_template('App/help.html')
    # return HttpResponse(template.render(help_dict,request))

def nice(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpages_list}
    return render(request,'App/get_data.html',date_dict)

def myext(request):
    print(request.POST['firstname'])
    return HttpResponse(request.POST['firstname'] + request.POST['lastname'])
# def myext(request):
#     # my_dict={'insert':"This is called through App->views->myext"}
#     return render(request,'contact/contact.html')
