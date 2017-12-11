from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import Account

class ProfileTemplateView(TemplateView):
    template_name = 'profile.html'

class BeginPageTemplateView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = super(BeginPageTemplateView, self).get_context_data(*args, **kwargs)
        queryset = Account.objects.all()
        hello="testing"
        var2="script"
        context = {"hello" : hello, "var2" : var2, "object_list" : queryset}
        return context

class LoginPageTemplateView(TemplateView):
    template_name = 'login.html'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class RegisterTemplateView(TemplateView):
    template_name = 'register.html'

class SearchAccountRecords(ListView):
    template_name = 'index.html'
    def get_queryset(self, **kwargs):
        print(self.kwargs)
        slug = self.kwargs.get('id')
        if slug:
            queryset = Account.objects.filter(
                Q(id_number__icontains=slug) |
                Q(first_name__icontains=slug) |
                Q(last_name__icontains=slug)              
                )
        else:
            queryset = Account.objects.none()
        return queryset