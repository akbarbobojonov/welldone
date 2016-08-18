import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    fullname = forms.CharField(max_length=128)
    phone = forms.CharField()
    accept_terms = forms.BooleanField()

    def clean_username(self):
        data = self.cleaned_data
        try:
            User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return data['username']
        raise forms.ValidationError(_("This username already exists."))

    def clean_email(self):
        data = self.cleaned_data
        try:
            User.objects.get(email=data['email'])
        except User.DoesNotExist:
            return data['email']
        raise forms.ValidationError(_("This email already exists."))

    def clean_phone(self):
        data = self.cleaned_data
        return data['phone']

    def save(self, request):
        data = self.cleaned_data

        user = User.objects.create_user(
            first_name=data['fullname'],
            last_name=data['phone'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
        )

        return True