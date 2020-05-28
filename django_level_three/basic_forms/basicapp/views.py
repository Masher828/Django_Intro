from django.shortcuts import render
from .forms import Form
from django import forms
# Create your views here.
def index(request):
    return render(request, 'htmls/index.html')

def formpage(request):
    form = Form()

    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid() :
            err = form.botcatcher( form.cleaned_data['botcatch'])
            if len(err) ==0 :
                raise forms.ValidationError(err)
            else:
                print("Validation Success")
                print('Name' , form.cleaned_data['name'])
                print('email' , form.cleaned_data['email'])
                print('Text' , form.cleaned_data['text'])
    return render(request,'htmls/formpage.html',{'formm' : form})
