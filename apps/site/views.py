from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "site/home.html"


class About(TemplateView):
    template_name = "site/about.html"


class Signup(TemplateView):
    template_name = "site/registration/signup.html"


class Login(TemplateView):
    template_name = "site/login.html"