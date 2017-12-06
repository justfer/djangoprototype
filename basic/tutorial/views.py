from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class ProfileTemplateView(TemplateView):
    template_name = 'profile.html'

class BeginPageTemplateView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = super(BeginPageTemplateView, self).get_context_data(*args, **kwargs)
        hello="testing"
        var2="script"
        context = {"hello" : hello, "var2" : var2}
        return context

class LoginPageTemplateView(TemplateView):
    template_name = 'login.html'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class RegisterTemplateView(TemplateView):
    template_name = 'register.html'