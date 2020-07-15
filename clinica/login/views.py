from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name ='login/home.html'
    login_url = 'login:login'
    #redirect_field_name = 'redirect_to'
