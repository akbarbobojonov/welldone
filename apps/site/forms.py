import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from datetime import timedelta
from django.utils import timezone
from django.utils.crypto import get_random_string


from apps.cprofile.models import CProfile


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    fullname = forms.CharField(max_length=128)
    phone = forms.CharField()
    accept_terms = forms.BooleanField(label=_("I agree to the terms and conditions"))

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
            is_active=False,
        )

        activation_key = get_random_string(64).lower()
        key_expires = timezone.now() + timedelta(days=1)

        profile = CProfile.objects.create(
            user=user,
            activation_key=activation_key,
            key_expires=key_expires,
        )

        profile.send_email_verified(request)

        return True