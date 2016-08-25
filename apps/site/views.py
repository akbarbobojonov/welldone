from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.contrib import messages

from .forms import *

from apps.cprofile.models import CProfile


class Home(TemplateView):
    template_name = "site/home.html"


class About(TemplateView):
    template_name = "site/about.html"


class Signup(TemplateView):
    template_name = "site/registration/signup.html"

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('home')
        return render(request, self.template_name, {
            'form': SignupForm()
        })

    def post(self, request):
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save(request)
            return redirect('signup_complete')
        
        return render(request, self.template_name, {'form': form})


class SignupComplete(TemplateView):
    template_name = "site/registration/signup_complete.html"


class EmailVerified(TemplateView):
    template_name = "site/registration/email_verified.html"

    def get(self, request, activation_key):

        try:
            cprofile = CProfile.objects.get(activation_key__exact=activation_key)
        except CProfile.DoesNotExist:
            return render(request, self.template_name, {'message': _("Activation key not found. The code may have expired.")})

        if not cprofile.confirm_activation_key():
            return render(request, self.template_name, {'message': _("Invalid activation key. The code may have expired.")})

        messages.success(request, _("Your account has been successfully activated. You can Log in."))

        return redirect('login')
