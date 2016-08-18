from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import *


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


class Login(TemplateView):
    template_name = "site/login.html"