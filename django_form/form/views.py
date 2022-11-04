from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def form(request):
    new_form = forms.user_form()
    diction = {'test_form': new_form}
    if request.method == 'POST':
        new_form = forms.user_form(request.POST)

        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']

            diction.update({'user_name':user_name})
            diction.update({'user_dob':user_dob})
            diction.update({'user_email':user_email})
            diction.update({'form_submited':"Yes"})

    return render(request, 'form/form.html' , context=diction)
