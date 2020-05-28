from django import forms

class Form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget= forms.Textarea)
    botcatch = forms.CharField(required = False, widget = forms.HiddenInput)

    def botcatcher(self,botcatch):
        botcatch = self.cleaned_data['botcatch']
        if len(botcatch)>0:
            return "Gotcha Bot"
        return ""
